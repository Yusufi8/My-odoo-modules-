from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    barcode = fields.Char(string='Barcode/QR Code')
    expiry_date = fields.Date(string='Expiry Date')
    batch_number = fields.Char(string='Batch Number')
    days_to_expiry = fields.Integer(string='Days to Expiry', compute='_compute_days_to_expiry', store=True)
    low_stock_threshold = fields.Integer(string='Low Stock Threshold', default=5)
    is_near_expiry = fields.Boolean(string='Near Expiry', compute='_compute_days_to_expiry', store=True)
    is_low_stock = fields.Boolean(string='Low Stock', compute='_compute_stock_status', store=True)

    @api.depends('expiry_date')
    def _compute_days_to_expiry(self):
        today = fields.Date.today()
        for product in self:
            if product.expiry_date:
                delta = (product.expiry_date - today).days
                product.days_to_expiry = delta
                product.is_near_expiry = delta <= 15
            else:
                product.days_to_expiry = 0
                product.is_near_expiry = False

    @api.depends('qty_available')
    def _compute_stock_status(self):
        for product in self:
            product.is_low_stock = product.qty_available <= product.low_stock_threshold
