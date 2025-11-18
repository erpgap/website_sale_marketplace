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
        """Auto-assign marketplace_vendor_id and setup dropshipping on creation"""
        vendor_partner = self._get_vendor_partner()
        is_portal_vendor = bool(vendor_partner)

        for vals in vals_list:
            # Auto-assign vendor if not already set and user is portal/vendor
            if not vals.get('marketplace_vendor_id') and vendor_partner:
                vals['marketplace_vendor_id'] = vendor_partner.id

        # Portal vendors need sudo to create products (stock module accesses routes in defaults)
        if is_portal_vendor:
            products = super(ProductTemplate, self.sudo()).create(vals_list)
            # Setup dropshipping and supplierinfo
            self.sudo()._setup_vendor_dropshipping(products, vendor_partner)
        else:
            products = super().create(vals_list)

        return products

    def _setup_vendor_dropshipping(self, products, vendor_partner):
        """Setup dropshipping and supplier info for vendor products"""
        # Get dropship route
        dropship_route = self.env.ref('stock_dropshipping.route_drop_shipping', raise_if_not_found=False)

        for product in products:
            if product.marketplace_vendor_id == vendor_partner:
                # Set dropship route
                if dropship_route:
                    product.write({
                        'route_ids': [(4, dropship_route.id)]
                    })

                # Create supplierinfo record
                self.env['product.supplierinfo'].create({
                    'partner_id': vendor_partner.id,
                    'product_tmpl_id': product.id,
                    'min_qty': 1.0,
                    'price': product.list_price or 0.0,
                })
