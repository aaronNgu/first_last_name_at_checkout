# -*- coding: utf-8 -*-
{
    'name': "First & Last Name at Checkout",
    'summary': "Separate first and last name fields at checkout and portal",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Website/Website',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['website_sale', 'partner_firstname'],
    'data': [
        'data/whitelist_fields.xml',
        'views/templates.xml',
    ],
}
