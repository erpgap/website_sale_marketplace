# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api,fields, models

class Website(models.Model):
    _inherit = 'website'

    is_marketplace_website = fields.Boolean(compute='_compute_is_marketplace_website', store=True, string="Marketplace Website")
    is_marketplace_website_child = fields.Boolean(
        related='parent_id.is_marketplace_website', readonly=True, string="Marketplace Contact")

    def _compute_is_marketplace(self):
        """
        Compute the is_marketplace field for each partner.
        This field indicates whether the partner is a marketplace or not.
        """
        for website in self:
            website.is_marketplace = website.is_marketplace_website or \
                                     website.parent_id.is_marketplace_website or False
