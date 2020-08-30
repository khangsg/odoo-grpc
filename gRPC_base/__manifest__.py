# -*- coding: utf-8 -*-
{
    'name': 'gRPC Base',
    'category': 'Base gRPC for Odoo',
    'author': 'khangnguyen16021990@gmail.com',
    'description': 'Simple Module implement gRPC in Odoo',
    "license": "LGPL-3",
    'depends': [
        'base',
        'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/gRPC_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}