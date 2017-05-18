# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Hr Payroll Advance Account',
    'version': '10.0.0.1.0',
    'category': 'Human Resources',
    'sequence': 36,
    'author': 'Joaquin Gutierrez',
    'website': 'http://www.gutierrezweb.es',
    'description': """
        Management advance payroll for employee
    """,
    'depends': [
        'hr',
        'hr_payroll',
        'hr_payroll_advance',
    ],
    'data': [
    ],
    'installable': False,
    'auto_install': False,
}
