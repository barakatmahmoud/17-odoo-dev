# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'version' : '17.1',
    'summary': 'Custom App Real Estate For Learning',
    'depends': ['base', 'mail','web'],
    'data': [
        'security/ir.model.access.csv',

        'data/sequence.xml',
        'data/mail_template.xml',
        'wizard/change_state_views.xml',

        'views/base_menus.xml',
        'views/property_views.xml',
        'views/owner_views.xml',
        'views/tag_views.xml',
        'views/res_partner_views.xml',
        'views/property_history.xml',
    ],
    'application': True,
}
