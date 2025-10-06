{
    'name': 'College ERP',
    'version': '18.0.1.0.0',
    'summary': 'Comprehensive College Management System - Manage Students, Courses, Departments',
    'description': """
        College ERP System
        ==================
        * Student Management with Automated Roll Numbers
        * Department and Course Management
        * Advanced Security with Role-based Access Control
        * Interactive Dashboard with Real-time Statistics
        * Student Enrollment Wizard
        * Excel Export Functionality with Filters
        * Professional PDF Reports
        * Automated Number Sequences
        * Activity Tracking and Logging
    """,
    'author': 'Yusuf Khan',
    'website': 'https://www.yourwebsite.com',
    'category': 'Education',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'views/menus.xml',
        'views/department_views.xml',
        'views/course_views.xml',
        'views/student_views.xml',
        'views/dashboard_views.xml',
        'views/enroll_wizard_views.xml',
        'views/export_student_wizard_views.xml',
        'reports/student_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'college_erp/static/src/css/dashboard.css',
            'college_erp/static/src/js/dashboard.js',
            'college_erp/static/src/xml/dashboard.xml',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}