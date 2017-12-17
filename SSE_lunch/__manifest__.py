# -*- coding: utf-8 -*-
{
    'name': "sse_lunch",

    'summary': """
        Extension for Lunch module for make favorite order and send email""",

    'description': """
        The features of Improvement for Lunch Order module is an extension of Lunch Order module. There are two major improvements:
        1. Send emails to vendors after every order line, enabling users to communicate their orders to vendors. This improvement is based on the existing feature to confirm order lines.
        2. Select order lines from favourite menu, allowing users to create quickly an order according to their most frequent order lines. This improvement is based on the existing feature to add order lines to a new order.
        user guide : https://github.com/BoomHelloWorld/sse_lunch2017/blob/master/Documentation/05-User-Guide.pdf
    """,

    'author': "Thu Nguyen and Jirakit Paitoonnaramit",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'employee',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web', 'decimal_precision','lunch'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'wizard/favorite_order_view.xml',
        'views/views.xml',
        'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
