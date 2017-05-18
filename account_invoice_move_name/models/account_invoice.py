# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def finalize_invoice_move_lines(self, move_lines):
        move_lines = super(
            AccountInvoice, self).finalize_invoice_move_lines(move_lines)
        for move in move_lines:
            if move[2]['name'] == '/':
                if self.type in ('in_invoice', 'in_refund'):
                    if self.reference:
                        move[2]['name'] = '%s - %s' % (
                            self.reference, self.number)
                    else:
                        move[2]['name'] = '%s' % self.number
                else:
                    move[2]['name'] = '%s' % self.number
        return move_lines
