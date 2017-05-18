# -*- coding: utf-8 -*-
# Copyright 2017 Joaquin Gutierrez Pedrosa <joaquin@gutierrezweb.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'account_invoice_currency_rate',
    'version': '10.0.1.0.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'description': """
    This module adds the field currency_rate on account invoice in order to
    force the currency rate on an invoice.
    """,
    'author': 'Joaquín Gutiérrez Pedrosa',
    'website': 'http://www.gutierrezweb.es',
    'depends': [
        'account'
    ],
    'data': [
        'wizard/force_currency_rate_view.xml',
        'views/invoice_view.xml',
    ],
    'installable': True,
}
