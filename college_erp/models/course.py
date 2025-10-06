from odoo import models, fields, api

class CollegeCourse(models.Model):
    _name = 'college.course'
    _description = 'College Course'

    name = fields.Char('Course Name', required=True)
    code = fields.Char('Course Code', readonly=True, copy=False)
    fee = fields.Float('Course Fee', default=0.0)
    department_id = fields.Many2one('college.department', string='Department')
    student_ids = fields.One2many('college.student', 'course_id', string='Students')

    @api.model
    def create(self, vals):
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('college.course') or '/'
        return super().create(vals)

    _sql_constraints = [
        ('course_code_unique', 'unique(code)', 'Course code must be unique!'),
    ]
