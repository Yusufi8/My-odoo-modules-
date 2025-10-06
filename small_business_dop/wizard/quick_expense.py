# -*- coding: utf-8 -*-
from odoo import models, fields

class QuickExpenseWizard(models.TransientModel):
    _name = 'business.quick.expense.wizard'
    _description = 'Quick Expense Wizard'

    name = fields.Char('Description', required=True)
    amount = fields.Monetary('Amount', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    employee_id = fields.Many2one('res.users', string='Submitted By')

    def action_create_expense(self):
        self.env['business.expense'].create({
            'name': self.name,
            'amount': self.amount,
            'currency_id': self.currency_id.id,
            'employee_id': self.employee_id.id,
        })
