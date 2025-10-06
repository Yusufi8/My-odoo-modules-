# -*- coding: utf-8 -*-
from odoo import models, fields

class BusinessStaff(models.Model):
    _name = 'business.staff'
    _description = 'Staff Record (lightweight)'

    name = fields.Char('Name', required=True)
    user_id = fields.Many2one('res.users', string='Related User')
    job_title = fields.Char('Job Title')
    active = fields.Boolean('Active', default=True)
