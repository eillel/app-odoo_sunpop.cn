# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    weight_total = fields.Float(string='Total Weight(kg)', compute='_compute_weight_total')

    def _compute_weight_total(self):
        for sale in self:
            weight_tot = 0
            for line in sale.order_line:
                if line.product_id:
                    weight_tot += line.weight_subtotal or 0.0
            sale.weight_total = weight_tot

