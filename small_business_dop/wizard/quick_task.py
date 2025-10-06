# -*- coding: utf-8 -*-
from odoo import models, fields

class QuickTaskWizard(models.TransientModel):
    _name = 'business.quick.task.wizard'
    _description = 'Quick Task Wizard'

    name = fields.Char('Title', required=True)
    assigned_to = fields.Many2one('res.users', string='Assign To')

    def action_create_task(self):
        self.env['daily.task'].create({
            'name': self.name,
            'assigned_to': self.assigned_to.id,
        })
