# -*- encoding: utf-8 -*-

{
    'name': 'Hs Code Advanced',
    'version': '10.0.1.0.0',
    'category': 'Stock',
    'sequence': 36,
    'author': 'Joaquin Gutierrez',
    'website': 'http://www.gutierrezweb.es',
    'description': """
    Convert hs_code field to one2many field. Add product.template.hscode object
    for enhancement utilization.
    """,
    'depends': [
        'delivery',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
