{
    'name': 'To Do List',
    'version': '17.0',
    'category': 'Productivity',
    'summary': 'Simple To Do List',
    'author': 'Barakt',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/to_do_list_views.xml',
    ],
    'application': True,
    'installable': True,
    'assets' : {
        'web.assets_backend': [
            'to_do_list_app/static/src/componentes/*/*.xml',
            'to_do_list_app/static/src/componentes/*/*.js'
        ]
    }
}