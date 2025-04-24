# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_marketplace_vendor = fields.Boolean(
        related='is_marketplace', store=True, string="Marketplace Vendor", readonly=True)
