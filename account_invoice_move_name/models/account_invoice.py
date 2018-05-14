# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def invoice_validate(self):
        invoices = super(AccountInvoice, self).invoice_validate()
        for invoice in self:
            for move in invoice.move_id:
                lines = move.line_ids.filtered(
                    lambda x: x.account_id.internal_type in [
                        'receivable', 'payable'])
                for line in lines:
                    if line.account_id.internal_type == 'receivable':
                        line.name = '%s' % invoice.number or invoice.ref
                    if line.account_id.internal_type == 'payable':
                        line.name = '%s - %s' % (
                            invoice.reference or '', invoice.number)
        return invoices
