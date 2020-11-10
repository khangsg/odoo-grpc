# -*- coding: utf-8 -*-
{
    'name': 'Get Odoo data from javascript using gRPC',
    'category': 'Base gRPC for Odoo',
    'author': 'KhangSG Solutions',
    'description': 'Simple Module implement gRPC in Odoo',
    "license": "AGPL-3",
    "website": "https://odoo-vn.com",
    'depends': [
        'base',
        'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/gRPC_view.xml'
    ],
    'images': [
            'static/description/banner.png',
        ],
    'installable': True,
    'application': False,
    'auto_install': False,
}