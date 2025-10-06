# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BusinessExpense(models.Model):
    _name = 'business.expense'
    _description = 'Business Expense'

    name = fields.Char('Description', required=True)
    employee_id = fields.Many2one('res.users', string='Submitted By')
    amount = fields.Monetary('Amount', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    state = fields.Selection([('draft','Draft'),('submitted','Submitted'),('approved','Approved'),('rejected','Rejected')], default='draft')
    date = fields.Date('Date', default=fields.Date.context_today)

    def action_submit(self):
        self.state = 'submitted'

    def action_approve(self):
        self.state = 'approved'

    def action_reject(self):
        self.state = 'rejected'
