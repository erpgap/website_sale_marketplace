# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api,fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_marketplace_company = fields.Boolean(
        compute='_compute_marketplace_user',
        string='Marketplace Company',
        help='Indicates whether the user is a seller on the marketplace.',
        readonly= False,
        store= True
    )

    @api.depends("is_marketplace_company")
    def _compute_marketplace_user(self):
        for partner in self:
            for child in partner.child_ids:
                child.is_marketplace_company = partner.is_marketplace_company
