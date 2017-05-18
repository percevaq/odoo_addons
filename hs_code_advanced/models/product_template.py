# -*- coding: utf-8 -*-
# Copyright 2017 Ancana Inversiones S.L. <joaquin.gutierrez@grupoancana.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import models, fields, api, _


class ProductTemplateHscode(models.Model):
    _name = 'product.template.hscode'
    _description = 'Product Template HS Code'
    _rec_name = 'code'

    code = fields.Char(
        string='Code',
        required=True,
        help="HS Code")
    description = fields.Text(
        string='Description',
        required=True,
        translate=True,
        help="HS Name")


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    hs_code_id = fields.Many2one(
        comodel_name='product.template.hscode',
        string='HS Code',
        required=False,
        help="Standardized code for international "
             "shipping and goods declaration")
