# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.


from openerp import models, fields, api, exceptions, _

import logging

_log = logging.getLogger(__name__)


class HrPaySlipRun(models.Model):
    _inherit = 'hr.payslip.run'

    mode_id = fields.Many2one(
        comodel_name='payment.mode',
        string='Payment Mode',
        required=True,
        help="Please select payment mode")
    date_maturity = fields.Date(
        string='Due date',
        required=True,
        default=fields.Date.today(),
        help="This field is used for payable and receivable journal entries. "
             "You can put the limit date for the payment of this line.")
    account_bank_mode = fields.Selection(
        string='Bank Mode',
        selection=[('employee', 'By Employee'),
                   ('partner', 'By Partner')],
        required=True,
        default='employee',
        help="By Employee: select bank account by employee data, By Partner: "
             "select bank account by partner associated to employee")
    state = fields.Selection(
        selection_add=[('posted', 'Posted'),
                       ('paid', 'Paid')])
    payment_order_id = fields.Many2one(
        comodel_name='payment.order',
        string='Payment Order',
        required=False,
        help="Payment Order")

    @api.one
    def draft_payslip_run(self):
        return self.write({'state': 'draft'})

    @api.one
    def posted_payslip_run(self):
        if self.slip_ids:
            for slip in self.slip_ids:
                slip.process_sheet()
        else:
            raise exceptions.Warning(_('No Payslip Line in process'))
        return self.write({'state': 'posted'})

    @api.one
    def paid_payslip_run(self):
        # TODO: Revisar asignacion de divisas y moneda de la compañia
        result = []
        for slip in self.slip_ids:
            result.append({
                'slip': slip,
                'line_id': slip.move_id.line_id.filtered(
                    lambda x: not x.reconcile_id and
                    x.account_id.type == 'payable')
            })
        if result:
            order_id = self.env['payment.order'].create({
                'mode': self.mode_id.id,
                'date_scheduled': self.date_maturity,
                'user_id': self.env.user.id,
                'payment_order_type': 'payment',
            })
            _log.info(self.env.context)
            for vals in result:
                slip_id = vals['slip']
                line_id = vals['line_id']
                if self.account_bank_mode == 'employee':
                    bank_id = slip_id.employee_id.bank_account_id
                else:
                    bank_id = \
                        slip_id.employee_id.user_id and \
                        slip_id.employee_id.user_id.partner_id and \
                        slip_id.employee_id.user_id.partner_id.bank_account_id
                self.env['payment.line'].create({
                    'partner_id': line_id.partner_id.id,
                    'bank_id': bank_id.id,
                    'communication': slip_id.name,
                    'name': line_id.name,
                    'order_id': order_id.id,
                    'amount_currency': line_id.credit,
                    'currency': line_id.currency_id.id or
                    order_id.company_id.currency_id.id,
                })
            return self.write({
                'state': 'paid', 'payment_order_id': 'order_id.id'})
        return False
