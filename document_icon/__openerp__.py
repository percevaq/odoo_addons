# -*- coding: utf-8 -*-
###############################################################################
#
#    Joaquin Gutierrez Pedrosa
#    Copyright (C) 2014-Today Joaquin Gutierrez Pedrosa <www.gutierrezweb.com>
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
###############################################################################
{
    'name': 'Document MineType Icons',
    'version': '8.0.1.0.0',
    'category': 'Knowledge Management',
    'license': 'LGPL-3',
    'author': 'Joaquin Gutierrez Pedrosa',
    'website': 'http://www.gutierrezweb.es/',
    'description': """
        Add minetype and icon image in popular file extension

        Icons images Designed by Freepik and distributed by Flaticon

        """,
    'depends': [
        'mail',
        'document',
    ],
    'data': [
        'data/document_icon_data.xml',
        'views/document_icon_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
