from odoo import models, fields

class EnrollWizard(models.TransientModel):
    _name = 'college.enroll.wizard'
    _description = 'Enroll Wizard'

    student_id = fields.Many2one('college.student', string='Student', required=True)
    course_ids = fields.Many2many('college.course', string='Courses')

    def action_enroll(self):
        # Create separate enrollment or assign first course for demo purposes
        for course in self.course_ids:
            # this demo assigns the last selected course to student's course_id
            self.student_id.course_id = course.id
        return {'type': 'ir.actions.act_window_close'}
