# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    marketplace_vendor_id = fields.Many2one('res.partner', string='Marketplace Vendor')
    description_ecommerce = fields.Html(
        string='eCommerce Description',
        translate=True,
        sanitize_attributes=False,
        sanitize_form=False
    )

    @api.model
    def _get_vendor_partner(self):
        """Get the vendor partner for the current user"""
        user = self.env.user

        # Portal users: return parent company if exists, otherwise themselves
        if user._is_portal():
            if user.partner_id.parent_id:
                return user.partner_id.parent_id
            else:
                return user.partner_id

        return None

    @api.model_create_multi
    def create(self, vals_list):
        """Auto-assign marketplace_vendor_id on creation if not set"""
        vendor_partner = self._get_vendor_partner()

        for vals in vals_list:
            # Auto-assign vendor if not already set and user is portal/vendor
            if not vals.get('marketplace_vendor_id') and vendor_partner:
                vals['marketplace_vendor_id'] = vendor_partner.id

        return super().create(vals_list)
