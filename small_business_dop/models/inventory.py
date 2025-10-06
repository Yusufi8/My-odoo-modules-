# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BusinessInventory(models.Model):
    _name = 'business.inventory'
    _description = 'Inventory Item'

    name = fields.Char('Item Name', required=True)
    quantity = fields.Integer('Quantity', default=0)
    location = fields.Char('Location')
    date = fields.Date('Date', default=fields.Date.context_today)

    @api.model
    def check_in(self, qty):
        self.quantity = (self.quantity or 0) + int(qty)

    @api.model
    def check_out(self, qty):
        if int(qty) <= (self.quantity or 0):
            self.quantity = (self.quantity or 0) - int(qty)
        else:
            raise ValueError('Not enough stock')
