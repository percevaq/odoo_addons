# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Hr Payroll Advance Account',
    'version': '11.0.0.1.0',
    'category': 'Human Resources',
    'sequence': 36,
    'summary': 'Payroll advances for employees with Account',
    'author': 'Joaquin Gutierrez',
    'website': 'http://www.gutierrezweb.es',
    'description': """
        Management advances payroll for employees with Account
    """,
    'depends': [
        'hr',
        'hr_payroll',
        'hr_payroll_advance',
    ],
    'data': [
        'views/hr_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
