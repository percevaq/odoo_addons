# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __manifest__.py file at the root folder of this module.

{
    'name': 'Website Portal for Human Resource',
    'category': 'Website',
    'summary': 'Employee Zone in web FrontEnd',
    'version': '10.0.1.0.0',
    'author': 'Ancana Inversiones, S.L.',
    'website': 'https://www.grupoancana.com/',
    'depends': [
        'document_icon',
        'hr_contract',
        'hr_payroll',
        'website_portal',
    ],
    'data': [
        'templates/website_portal_hr.xml',
    ],
    'demo': [
    ],
    'license': 'LGPL-3',
    'installable': True,
}
