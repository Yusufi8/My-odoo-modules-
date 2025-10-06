from odoo import models, fields, api

class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'College Student'
    _rec_name = 'name'

    name = fields.Char('Student Name', required=True)
    roll_number = fields.Char('Roll Number', readonly=True, copy=False)
    user_id = fields.Many2one('res.users', string='Related User')
    course_id = fields.Many2one('college.course', string='Course')
    department_id = fields.Many2one('college.department', string='Department', store=True)

    total_fee = fields.Float('Total Fee', compute='_compute_total_fee', store=True)
    attendance_percentage = fields.Float('Attendance %', compute='_compute_attendance', store=False)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('graduated', 'Graduated'),
        ('alumni', 'Alumni'),
    ], default='draft', string='Status')

    @api.model
    def create(self, vals):
        if not vals.get('roll_number'):
            vals['roll_number'] = self.env['ir.sequence'].next_by_code('college.student') or '/'
        return super().create(vals)

    @api.onchange('course_id')
    def _onchange_course(self):
        if self.course_id:
            self.department_id = self.course_id.department_id

    @api.depends('course_id.fee')
    def _compute_total_fee(self):
        for rec in self:
            rec.total_fee = rec.course_id.fee * 1.18 if rec.course_id and rec.course_id.fee else 0.0

    @api.depends('course_id')
    def _compute_attendance(self):
        for rec in self:
            # Placeholder: implement attendance computation based on attendance records if added
            rec.attendance_percentage = 0.0

    def action_activate(self):
        self.write({'state': 'active'})

    def action_graduate(self):
        self.write({'state': 'graduated'})

    def action_alumni(self):
        self.write({'state': 'alumni'})

    _sql_constraints = [
        ('roll_number_unique', 'unique(roll_number)', 'Roll Number must be unique!'),
    ]
