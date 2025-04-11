# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api,fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_marketplace = fields.Boolean(compute='_compute_is_marketplace', store=True, string="Marketplace")
    is_marketplace_vendor = fields.Boolean("Marketplace Vendor", default=False)
    is_marketplace_vendor_child = fields.Boolean(
        related='parent_id.is_marketplace_vendor', readonly=True, string="Marketplace Contact")

    def _compute_is_marketplace(self):
        """
        Compute the is_marketplace field for each partner.
        This field indicates whether the partner is a marketplace or not.
        """
        for partner in self:
            partner.is_marketplace = partner.is_marketplace_vendor or \
                                     partner.parent_id.is_marketplace_vendor or False
