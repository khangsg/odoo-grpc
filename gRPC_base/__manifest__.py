# -*- coding: utf-8 -*-
{
    'name': 'Get Odoo data from javascript using gRPC',
    'category': 'Base gRPC for Odoo',
    'author': 'khangnguyen16021990@gmail.com',
    'description': 'Simple Module implement gRPC in Odoo',
    "license": "LGPL-3",
    "website": "https://github.com/khangsg/odoo-grpc",
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