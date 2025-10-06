# -*- coding: utf-8 -*-
from odoo import models, fields

class DailyTask(models.Model):
    _name = 'daily.task'
    _description = 'Daily Task'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    state = fields.Selection([('draft','Draft'),('in_progress','In Progress'),('done','Done')], default='draft')
    date_deadline = fields.Date('Deadline')
    create_date = fields.Datetime('Created', readonly=True)
