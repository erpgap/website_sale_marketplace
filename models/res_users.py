# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_marketplace_seller = fields.Boolean(
        related='partner_id.is_marketplace_company',
        string='Marketplace Vendor',
        help='Indicates whether the user is a seller on the marketplace.',
        readonly=False,
        store=True
    )
    is_portal_user = fields.Boolean(
        string="É Usuário Portal",
        compute='_compute_is_portal_user',
        store=False
    )

    @api.depends('groups_id')
    def _compute_is_portal_user(self):
        portal_group = self.env.ref('base.group_portal')
        for user in self:
            user.is_portal_user = portal_group in user.groups_id