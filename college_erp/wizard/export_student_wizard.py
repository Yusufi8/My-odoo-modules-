from odoo import models, fields
import io
import xlsxwriter
import base64

class ExportStudentWizard(models.TransientModel):
    _name = 'export.student.wizard'
    _description = 'Export Students to Excel'

    file_name = fields.Char('File Name', default='students.xlsx')
    file_data = fields.Binary('Excel File', readonly=True)
    student_ids = fields.Many2many('college.student', string='Select Students')

    def action_export(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Students')
        headers = ['Roll Number', 'Name', 'Course', 'Department', 'Total Fee']
        for col, header in enumerate(headers):
            sheet.write(0, col, header)
        for row, student in enumerate(self.student_ids, start=1):
            sheet.write(row, 0, student.roll_number or '')
            sheet.write(row, 1, student.name or '')
            sheet.write(row, 2, student.course_id.name or '')
            sheet.write(row, 3, student.department_id.name or '')
            sheet.write(row, 4, student.total_fee or 0.0)
        workbook.close()
        output.seek(0)
        self.file_data = base64.b64encode(output.read())
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'export.student.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }
