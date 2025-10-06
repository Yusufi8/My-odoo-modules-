from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    department_id = fields.Many2one('college.department', string='Department', help='Department for teacher users')
