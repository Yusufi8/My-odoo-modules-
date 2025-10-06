{
    'name': 'Small Business DOP',
    'version': '18.0.1.0.0',
    'summary': 'Comprehensive Small Business Management System',
    'description': """
        Small Business Management System
        ===============================
        * Dashboard, Expense, Inventory, Staff, Task Management
        * Advanced Security and Access Rights
        * Interactive Dashboard (if present)
        * Automated Sequences
        * Activity Tracking
    """,
    'author': 'Yusuf Khan',
    'website': 'https://www.yourwebsite.com',
    'category': 'Business',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/dashboard_views.xml',
        'views/expense_views.xml',
        'views/inventory_views.xml',
        'views/staff_views.xml',
        'views/task_views.xml',
        'views/wizard_views.xml',
        'report/report_expense_views.xml',
        'report/report_inventory_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
