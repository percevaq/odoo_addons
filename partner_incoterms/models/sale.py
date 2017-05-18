# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id:
            self.incoterm = self.partner_id.property_sale_incoterm or None
