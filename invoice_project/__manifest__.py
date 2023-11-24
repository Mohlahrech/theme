# -*- coding: utf-8 -*-
{
    'name': "invoice_project",

    'summary': """
        Crée un projet à partir d'un devis article consommable""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Moh",
    'website': "https://cv-lahrech-mohamed.onrender.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','stock'],

    # always loaded
    'data': [
        'views/products.xml',

    ],
}
