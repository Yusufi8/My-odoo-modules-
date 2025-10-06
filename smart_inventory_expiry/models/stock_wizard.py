from odoo import models, fields
from odoo.exceptions import UserError

class StockScanWizard(models.TransientModel):
    _name = 'stock.scan.wizard'
    _description = 'Scan Product to Update Stock'

    barcode = fields.Char(string='Scan Barcode')
    quantity = fields.Float(string='Quantity')

    def update_stock(self):
        product = self.env['product.product'].search([('barcode', '=', self.barcode)], limit=1)
        if product:
            product.qty_available += self.quantity
            return {'type': 'ir.actions.client', 'tag': 'reload'}
        else:
            raise UserError('Product not found!')
