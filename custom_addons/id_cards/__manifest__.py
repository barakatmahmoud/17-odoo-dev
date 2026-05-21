# -*- coding: utf-8 -*-
{
    'name': 'ID CARDS',
    'description': "ID Cards",
    'version' : '17.1',
    'summary': 'Custom App For Portal User To Create Id Card',
    'depends': ['base','website'],
    'data': [
        'security/ir.model.access.csv',
       'views/base_menus.xml',
       'views/id_cards_request_views.xml',
       'views/id_cards_request_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'id_cards/static/src/js/id_cards_validation.js',
            'id_cards/static/src/js/id_cards_change.js',
        ],
    },
    'application': True,
}
