{
    'name': 'Hospital YK',
    'version': '18.0.1.0.0',
    'summary': 'Comprehensive Hospital Management System',
    'description': """
        Hospital Management System
        =========================
        * Patient, Appointment, Tag Management
        * Advanced Security and Access Rights
        * Interactive Dashboard (if present)
        * Automated Sequences
        * Activity Tracking
    """,
    'author': 'Yusuf Khan',
    'website': 'https://www.yourwebsite.com',
    'category': 'Healthcare',
    'depends': ['base', 'web', 'mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient_views.xml',
        'views/patient_readonly_views.xml',
        'views/appointment_views.xml',
        'views/patient_tag_views.xml',
        'views/appointment_line_views.xml',
        'views/menu.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
