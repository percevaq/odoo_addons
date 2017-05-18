# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Account Tag State",
    'version': "10.0.1.0.0",
    'summary': "View Tag state in account",
    'sequence': 51,
    'category': "Accounting",
    'author': "Joaquin Gutierrez Pedrosa,"
              "Odoo Community Association (OCA)",
    'license': "AGPL-3",
    'website': "https://www.gutierrezweb.es",
    'images': [
    ],
    'depends': [
        "account",
    ],
    'data': [
        "views/account_view.xml",
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
