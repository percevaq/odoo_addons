# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Document MimeType Icons',
    'version': '11.0.1.0.0',
    'category': 'Knowledge Management',
    'sequence': 36,
    'summary': 'Add icons based in MimeType Files',
    'license': 'LGPL-3',
    'author': 'Joaquin Gutierrez Pedrosa',
    'website': 'http://www.gutierrezweb.es/',
    'description': """
        Add mimetype and icon image in popular file extension
        Icons images Designed by Freepik and distributed by Flaticon
        """,
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'data/ir_attachment_mimetype_data.xml',
        'views/ir_attachment_views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
