# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BusinessDashboard(models.Model):
    _name = 'business.dashboard'
    _description = 'Dashboard Metrics'

    tasks_done = fields.Integer('Tasks Done', compute='_compute_metrics')
    expenses_approved = fields.Integer('Expenses Approved', compute='_compute_metrics')
    low_stock = fields.Integer('Low Stock Items', compute='_compute_metrics')

    @api.depends()
    def _compute_metrics(self):
        for rec in self:
            rec.tasks_done = self.env['daily.task'].search_count([('state','=','done')])
            rec.expenses_approved = self.env['business.expense'].search_count([('state','=','approved')])
            rec.low_stock = self.env['business.inventory'].search_count([('quantity','<',5)])
