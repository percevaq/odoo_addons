# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.


from odoo import models, fields, api, _


class HrPaySlipAdvance(models.Model):
    _name = 'hr.payslip.advance'
    _description = 'PaySlip Advance'

    @api.model
    def _default_currency(self):
        return self.env.user.company_id.currency_id

    name = fields.Char(
        string='Code',
        required=True,
        readonly=True,
        default='/',
        help="Code")
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
        required=True,
        help="Employee")
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        required=True,
        ondelete='set null',
        default=lambda self: self.env.user.company_id.id)
    state = fields.Selection(
        selection=[('draft', 'Draft'),
                   ('pending', 'Pending'),
                   ('done', 'Done')],
        string='Status',
        index=True,
        readonly=True,
        copy=False,
        default='draft',
        help="Status")
    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.today(),
        help="Date")
    amount = fields.Monetary(
        string='Amount',
        currency_field='currency_id')
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        required=True,
        readonly=True,
        default=_default_currency)
    note = fields.Text(
        string='Notes',
        required=False,
        help="Internal notes")

    _sql_constraints = [
        ('payslip_advance_unique_code', 'UNIQUE (name)',
         _('The code must be unique!')),
    ]

    @api.model
    def create(self, values):
        if values.get('name', '/') == '/':
            values['name'] = self.env['ir.sequence'].get('hr.payslip.advance')
        return super(HrPaySlipAdvance, self).create(values)

    @api.one
    def copy(self, default=None):
        if default is None:
            default = {}
        default['name'] = self.env['ir.sequence'].get('hr.payslip.advance')
        return super(HrPaySlipAdvance, self).copy(default)

    @api.one
    def action_pending(self):
        self.state = 'pending'

    @api.one
    def action_done(self):
        self.state = 'done'

    class HrEmployee(models.Model):
        _inherit = 'hr.employee'

        @api.multi
        def _compute_advance_count(self):
            for employee in self:
                employee.advance_count = len(employee.advance_ids)

        @api.multi
        def _compute_advance_amount(self):
            for employee in self:
                advance_ids = employee.advance_ids.filtered(
                    lambda x: x.state == 'pending')
                employee.advance_amount = sum(x.amount for x in advance_ids)
                _log.info(sum(x.amount for x in advance_ids))

        advance_ids = fields.One2many(
            comodel_name='hr.payslip.advance',
            inverse_name='employee_id',
            string='Payslip advance',
            required=False,
            help="Payslip advance list")
        advance_count = fields.Integer(
            string='Payslips',
            compute=_compute_advance_count)
        advance_amount = fields.Float(
            string='Advance Amount',
            compute=_compute_advance_amount)
