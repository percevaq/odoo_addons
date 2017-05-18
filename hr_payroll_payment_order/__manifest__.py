# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Hr Payroll Payment Order',
    'version': '10.0.1.0.1',
    'category': 'Human Resources',
    'sequence': 36,
    'author': 'Joaquin Gutierrez',
    'website': 'http://www.gutierrezweb.es',
    'description': """
    HR Payroll Payment Order using SEPA Credit Transfer
    """,
    'depends': [
        'hr',
        'hr_payroll',
        'hr_payroll_account',
        'account_banking_sepa_credit_transfer'
    ],
    'data': [
        'views/hr_payroll_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
