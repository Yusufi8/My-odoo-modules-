{
    'name': 'Smart Inventory & Expiry Manager',
    'version': '1.0',
    'author': 'Yusuf Khan',
    'depends': ['base', 'product'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/stock_product_views.xml',
        'views/stock_dashboard_views.xml',
        'views/stock_scan_wizard_views.xml',
        'views/stock_report_templates.xml',
        'data/automated_actions.xml',
    ],
    'application': True,
}