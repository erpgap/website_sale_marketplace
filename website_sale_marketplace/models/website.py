# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api,fields, models

class Website(models.Model):
    _inherit = 'website'

    is_marketplace = fields.Boolean(compute='_compute_is_marketplace', store=True, string="Marketplace")
    is_marketplace_website = fields.Boolean("Marketplace Vendor", default=False)

    def _compute_is_marketplace(self):

        for website in self:
            website.is_marketplace = website.is_marketplace_website or False
