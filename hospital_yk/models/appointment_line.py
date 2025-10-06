from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'Hospital Appointment Line'

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment", required=True)
    product_id = fields.Many2one('product.product', string="Product", required=True)
    qty = fields.Float(string="Quantity", required=True)
    appointment_line_ids = fields.One2many('hospital.appointment.line', 'appointment_id', string="Lines")
