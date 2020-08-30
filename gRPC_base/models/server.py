import grpc
from concurrent import futures
import time

from . import base_pb2
from . import base_pb2_grpc

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import Warning, UserError
import logging
import threading
_logger = logging.getLogger(__name__)

grpc_servers = {}


class ProductServicer(base_pb2_grpc.ProductsServicer):
    def __init__(self, cr):
        self.env = api.Environment(cr, SUPERUSER_ID, {})

    def GetProductInfo(self, request, context):
        _logger.info('System received a request to get product infor!')
        response = base_pb2.ProductResponse()
        product_rcs = self.env['product.product'].browse(request.product_id)
        response.name = product_rcs.name
        response.public_price = str(product_rcs.list_price)
        return response


class GrpcServerUi(models.Model):
    _name = 'grpc.server.uid'
    _description = _('GRPC Server')

    name = fields.Char(string='Name')
    listen_port = fields.Integer(string='Listening Port')
    create_date = fields.Datetime(string='Create Date')
    create_uid = fields.Many2one('res.users', string='Create By')
    state = fields.Selection([('running', 'Running'), ('stopped', 'Stopped')], string='Status',
                             default='stopped')

    _sql_constraints = [
        ('listen_port_uniq', 'unique (listen_port)', 'The listen port must be unique !')
    ]

    def grpc_woker(self):
        with api.Environment.manage():
            # As this function is in a new thread, I need to open a new cursor, because the old one may be closed
            new_cr = self.pool.cursor()
            self = self.with_env(self.env(cr=new_cr))
            server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
            base_pb2_grpc.add_ProductsServicer_to_server(ProductServicer(self.env.cr), server)
            _logger.info('Starting server. Listening on port %s.' % self.listen_port)
            server.add_insecure_port('[::]:%s' % self.listen_port)
            grpc_servers.update({self.id: server})
            server.start()
            server.wait_for_termination()

    def action_start(self):
        self.write({'state': 'running'})
        t = threading.Thread(name="%s.Bus" % self.name, target=self.grpc_woker)
        t.daemon = True
        t.start()

    def action_stop(self):
        self.write({'state': 'stopped'})
        if grpc_servers.get(self.id, False):
            _logger.info('Stopping server on port %s.' % self.listen_port)
            grpc_servers.get(self.id).stop(0)
