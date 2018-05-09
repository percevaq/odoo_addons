# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.


from odoo import models, fields


class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'

    insurance_company = fields.Monetary(
        string='Company Insurance',
        required=True,
        help="Company Insurance")
    insurance_employee = fields.Monetary(
        string='Employee Insurance',
        required=True,
        help="Employee Insurance")
    retention_employee = fields.Float(
        string='Employee Retention',
        required=True,
        help="Employee Retentions")
