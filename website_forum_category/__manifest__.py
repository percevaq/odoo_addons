# -*- encoding: utf-8 -*-

{
    'name': 'Website Forum Category',
    'version': '10.0.1.0.0',
    'category': 'Website',
    'sequence': 36,
    'author': 'Joaquin Gutierrez',
    'website': 'http://www.gutierrezweb.es',
    'description': """
    Add category to forum
    """,
    'depends': [
        'website_forum',
    ],
    'data': [
        'views/forum_view.xml',
        'templates/website_forum_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
