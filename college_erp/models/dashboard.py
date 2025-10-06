from odoo import models, fields, api

class CollegeDashboard(models.Model):
    _name = 'college.dashboard'
    _description = 'College ERP Dashboard'

    student_count = fields.Integer('Total Students', compute='_compute_stats')
    department_count = fields.Integer('Total Departments', compute='_compute_stats')
    total_fees = fields.Float('Total Fees Collected', compute='_compute_stats')

    @api.depends()
    def _compute_stats(self):
        Student = self.env['college.student']
        Department = self.env['college.department']
        for rec in self:
            rec.student_count = Student.search_count([])
            rec.department_count = Department.search_count([])
            rec.total_fees = sum(Student.search([]).mapped('total_fee') or [])
