from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment Manager'
    _rec_name = 'patient_id'

    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: ('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True, tracking=True)
    appointment_date = fields.Datetime(string="Appointment Date", required=True, tracking=True)
    note = fields.Text(string="Note", tracking=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ongoing', 'Ongoing'), ('done', 'Done'),
         ('cancelled', 'Cancelled')],
        string="Status", default='draft', tracking=True
    )
    @api.model
    def create(self, vals):
        if vals.get('reference', ('New')) == ('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or ('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def action_confirm(self):
        for record in self:
            if record.state != 'draft':
                raise UserError("Only draft appointments can be confirmed.")
            record.state = 'confirmed'
            record.message_post(body="Appointment confirmed.")

    def action_done(self):
        for record in self:
            if record.state != 'confirmed':
                raise UserError("Only confirmed appointments can be marked as done.")
            record.state = 'done'
            record.message_post(body="Appointment marked as done.")

    def action_ongoing(self):
        for record in self:
            if record.state != 'confirmed':
                raise UserError("Only confirmed appointments can be marked as ongoing.")
            record.state = 'ongoing'
            record.message_post(body="Appointment is now ongoing.")

    def action_cancel(self):
        for record in self:
            if record.state == 'done':
                raise UserError("Completed appointments cannot be cancelled.")
            record.state = 'cancelled'
            record.message_post(body="Appointment cancelled.")

