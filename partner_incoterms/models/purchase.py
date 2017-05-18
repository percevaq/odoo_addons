# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.

from odoo import models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('partner_id','company_id')
    def onchange_partner_id(self):
        if self.partner_id:
            self.incoterm_id = self.partner_id.property_purchase_incoterm or None
