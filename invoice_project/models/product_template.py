# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = "product.template"


    detailed_type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Déstiné à la vente')], string='Product Type', default='service', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')

    type = fields.Selection(
        [('consu', 'Consumable',),
         ('service', 'Déstiné à la vente')],
        compute='_compute_type', store=True, readonly=False, precompute=True)

class SaleOrderLine2(models.Model):
        _inherit = "product.template"


        detailed_type = fields.Selection(selection_add=[
            ('product', 'Storable Product')
        ], tracking=True, ondelete={'product': 'set consu'})
        type = fields.Selection(selection_add=[
            ('product', 'Storable Product')
        ], ondelete={'product': 'set consu'})
