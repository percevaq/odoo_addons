# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class InvoiceForceCurrencyRate(models.TransientModel):
    _name = 'invoice.force.currency.rate'
    _description = 'Force currency rate'

    @api.multi
    def _get_currency_rate(self):
        rate = 1
        if self.env.context.get('active_id'):
            invoice = self.env['account.invoice'].browse(
                self.env.context.get('active_id'))
            rate = invoice.currency_id.rate
        return rate

    currency_rate = fields.Float(
        string='Forced currency rate',
        default=_get_currency_rate,
        help="You can force the currency rate on the invoice with this field.")

    @api.multi
    def force_currency_rate(self):
        self.ensure_one()
        if self.env.context.get('active_id'):
            active_id = self.env.context.get('active_id')
            invoice = self.env['account.invoice'].browse(active_id)
            invoice.currency_rate = self.currency_rate
        return {'type': 'ir.actions.act_window_close'}
