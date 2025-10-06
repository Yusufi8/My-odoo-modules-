from odoo import models, fields, api

class CollegeDepartment(models.Model):
    _name = 'college.department'
    _description = 'College Department'

    name = fields.Char('Department Name', required=True)
    code = fields.Char('Department Code', required=True)
    course_ids = fields.One2many('college.course', 'department_id', string='Courses')
    student_ids = fields.One2many('college.student', 'department_id', string='Students')

    student_count = fields.Integer('Student Count', compute='_compute_student_count', store=True)

    @api.depends('student_ids')
    def _compute_student_count(self):
        for rec in self:
            rec.student_count = len(rec.student_ids)

    _sql_constraints = [
        ('dept_code_unique', 'unique(code)', 'Department code must be unique!'),
    ]
