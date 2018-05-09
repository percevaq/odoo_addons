# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Hr Payroll Advance',
    'version': '11.0.0.1.0',
    'category': 'Human Resources',
    'sequence': 36,
    'summary': 'Payroll advances for employees',
    'author': 'Joaquin Gutierrez',
    'website': 'http://www.gutierrezweb.es',
    'description': """
    Management advances payroll for employees
    """,
    'depends': [
        'hr',
        'hr_payroll',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/hr_sequence.xml',
        'views/hr_view.xml',
        'reports/advance_receipt.xml',
    ],
    'installable': True,
    'auto_install': False,
}
