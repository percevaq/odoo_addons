# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_sale_incoterm = fields.Many2one(
        string='Sales Incoterm',
        comodel_name='stock.incoterms',
        help='Default Incoterm used in a Sale Order when this partner is '
        'selected as the Customer.')
    property_purchase_incoterm = fields.Many2one(
        string='Purchases Incoterm',
        comodel_name='stock.incoterms',
        company_dependent=True,
        help='Default Incoterm used in a Purchase Order when this partner is '
        'selected as the Supplier.')
