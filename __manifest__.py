{
    'name': "Family Data",
    'author': 'Datasoup',
    'version': "16.0.1.0",
    'depends': ['base','hr'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/family_data_views.xml',
    ],
    'demo': [],
    'assets': {
    'web.assets_backend': [
        'family_data/static/src/scss/styles.scss',
    ]},
    'summary': "family Data",
    'description': "",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': True
}
