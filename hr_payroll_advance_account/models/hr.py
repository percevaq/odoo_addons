# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.


from odoo import models, fields


class HrPaySlipAdvance(models.Model):
    _inherit = 'hr.payslip.advance'

    journal_id = fields.Many2one(
        comodel_name='account.journal',
        string='Payment Method',
        readonly=True,
        states={'draft': [('readonly', False)]},
        required=True)
    move_id = fields.Many2one(
        comodel_name='account.move',
        string='Journal Entry',
        readonly=True,
        index=True,
        ondelete='restrict',
        copy=False,
        help="Link to the automatically generated Journal Items.")
