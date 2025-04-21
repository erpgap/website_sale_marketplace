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
        'website_sale',
        'portal',
        'contacts',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/res_partner_views.xml',
        'views/website_views.xml',
    ],
    'installable': True,
    'application': False,
}
