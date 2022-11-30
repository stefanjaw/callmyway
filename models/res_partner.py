# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerInherit(models.Model):
    
    _inherit = 'res.partner'
    product_id = fields.Many2one('product.product', string="Product")
    
