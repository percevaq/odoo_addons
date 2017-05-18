# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Spain - Payroll',
    'summary': 'Hr Payroll adapts to Spain',
    'version': '10.0.1.0.0',
    'category': 'Localization',
    'sequence': 35,
    'author': 'Joaquin Gutierrez',
    'website': 'http://www.gutierrezweb.es/',
    'description': """Management PaySlip for Spain""",
    'depends': [
        'hr_payroll'
    ],
    'data': [
        'view/hr_payroll_view.xml',
        'data/hr_payroll_data.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
