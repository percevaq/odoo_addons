# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Incoterms',
    'version': '10.0.1.0.0',
    'author': 'Joaquin Gutierrez Pedrosa',
    'website': 'http://www.gutierrezweb.es',
    'depends': [
        'purchase',
        'sale',
        'stock',
    ],
    'category': 'Partner',
    'description': """
    Adds a default purchase incoterm to the partner object which will be copied
    onto the Purchase Order incoterm as default.
    """,
    'data': [
        'views/res_partner.xml',
    ],
    'active': False,
    'installable': True
}
