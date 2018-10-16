# -*- coding: utf-8 -*-
{
    'name': "custom_invoice",

    'summary': """
        This Module customizes default invoice""",

    'description': """
         This Module customizes default invoice Template
    """,

    'author': "My Company",
    'website': "http://www.perkup.pk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}