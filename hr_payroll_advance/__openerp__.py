# -*- encoding: utf-8 -*-
##############################################################################
#
#    Joaquin Gutierrez Pedrosa
#    Copyright (C) 2016-Today Joaquin Gutierrez Pedrosa <www.gutierrezweb.es>
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
    'name': 'Hr Payroll Advance',
    'version': '8.0.0.1.0',
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
