# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Marketplace',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'Post, Sell, its your marketplace',
    'description': """ """,
    'depends': [
        'base',
        'website',
        'portal',
        'product',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/marketplace_users_views.xml',
    #    'views/marketplace_company_views.xml'
    ],
    'installable': True,
    'application': False,
}
