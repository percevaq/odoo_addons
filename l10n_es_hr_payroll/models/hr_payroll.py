# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.


from odoo import models, fields
import odoo.addons.decimal_precision as dp


class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'

    insurance_company = fields.Float(
        string='Company Insurance',
        digits=dp.get_precision('Account'),
        required=True,
        help="Company Insurance")
    insurance_employee = fields.Float(
        string='Employee Insurance',
        digits=dp.get_precision('Account'),
        required=True,
        help="Employee Insurance")
    retention_employee = fields.Float(
        string='Employee Retention',
        digits=dp.get_precision('Account'),
        required=True,
        help="Employee Retentions")
