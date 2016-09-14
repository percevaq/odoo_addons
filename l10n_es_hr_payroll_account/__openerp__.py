# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Joaquin Gutierrez Pedrosa All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Spain - Payroll with Accounting',
    'summary': 'Hr Payroll adapts to Spain with accounting',
    'version': '8.0.1.0.0',
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
