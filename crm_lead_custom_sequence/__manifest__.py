{
    'name': 'Custom Lead Sequence',
    'version': '18.0.1.0',
    'summary': 'Custom Lead Sequence, CRM Lead sequence, Lead sequence, Type Lead sequence, Sequence, CRM Sequence',
    'author': 'Tech GMB',
    # 'website': '',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': ['base', 'crm'],

    'data': [
        'data/data.xml',
        'views/crm_lead_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True
}
