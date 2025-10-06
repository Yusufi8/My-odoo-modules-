{
    'name': 'Smart Inventory Expiry',
    'version': '18.0.1.0.0',
    'summary': 'Comprehensive Inventory Expiry Management System',
    'description': """
        Smart Inventory Expiry System
        ============================
        * Product, Expiry, Wizard Management
        * Advanced Security and Access Rights
        * Interactive Dashboard (if present)
        * Automated Actions
        * Activity Tracking
    """,
    'author': 'Yusuf Khan',
    'website': 'https://www.yourwebsite.com',
    'category': 'Inventory',
    'depends': ['base', 'web', 'mail', 'product'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/stock_product_views.xml',
        'views/stock_dashboard_views.xml',
        'views/stock_scan_wizard_views.xml',
        'views/stock_report_templates.xml',
        'data/automated_actions.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}