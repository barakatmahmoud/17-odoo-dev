# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'version' : '17.1',
    'summary': 'Custom App Real Estate For Learning',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',

        'views/base_menus.xml',
        'views/property_views.xml',
        'views/owner_views.xml',
        'views/tag_views.xml',
        'views/res_partner_views.xml',
    ],
    'application': True,
}
