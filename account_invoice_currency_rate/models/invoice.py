# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def _show_force_currency(self):
        for invoice in self:
            if invoice.state == 'draft' \
                    and invoice.currency_id != invoice.company_id.currency_id:
                invoice.show_force_currency = True
            else:
                invoice.show_force_currency = False

    currency_rate = fields.Float(
        string='Forced currency rate',
        help="You can force the currency rate on the invoice with this field.")
    show_force_currency = fields.Boolean(
        string='Show force currency',
        compute=_show_force_currency)

    @api.multi
    def compute_invoice_totals(self, company_currency, invoice_move_lines):
        total = 0
        total_currency = 0
        for line in invoice_move_lines:
            if self.currency_id != company_currency:
                currency = self.currency_id.with_context(
                    date=self.date_invoice or fields.Date.context_today(self))
                if not line.get('currency_id') and line.get('amount_currency'):
                    line['currency_id'] = currency.id
                    line['amount_currency'] = currency.round(line['price'])
                    if self.currency_rate != 0:
                        line['price'] = line['price'] * self.currency_rate
                        line['price'] = currency.round(line['price'])
                    else:
                        line['price'] = currency.compute(
                            line['price'], company_currency)
            else:
                line['currency_id'] = False
                line['amount_currency'] = False
                line['price'] = self.currency_id.round(line['price'])
            if self.type in ('out_invoice', 'in_refund'):
                total += line['price']
                total_currency += line['amount_currency'] or line['price']
                line['price'] = - line['price']
            else:
                total -= line['price']
                total_currency -= line['amount_currency'] or line['price']
        return total, total_currency, invoice_move_lines
