# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Spain - Payroll with Accounting',
    'summary': 'Hr Payroll adapts to Spain with accounting',
    'version': '10.0.1.0.0',
    'category': 'Localization',
    'sequence': 36,
    'author': 'Joaquin Gutierrez',
    'website': 'http://www.gutierrezweb.es',
    'description': """Accounting Data for Spain Payroll Rules""",
    'depends': [
        'l10n_es_hr_payroll',
        'hr_payroll_account',
        'l10n_es'
    ],
    'data': [
        'data/l10n_es_hr_payroll_account_data.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
