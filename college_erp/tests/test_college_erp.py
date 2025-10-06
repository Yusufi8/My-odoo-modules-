from odoo.tests import TransactionCase

class TestCollegeERP(TransactionCase):

    def setUp(self):
        super().setUp()
        self.dept = self.env['college.department'].create({'name': 'Computer Science', 'code': 'CS'})
        self.course = self.env['college.course'].create({'name': 'Python', 'code': 'PY101', 'fee': 5000, 'department_id': self.dept.id})
        self.student = self.env['college.student'].create({'name': 'Yusuf', 'roll_number': 'STU0001', 'course_id': self.course.id})

    def test_department_student_count(self):
        self.assertEqual(self.dept.student_count, 1)

    def test_onchange_course_sets_department(self):
        self.assertEqual(self.student.department_id, self.dept)

    def test_total_fee_computation(self):
        self.assertAlmostEqual(self.student.total_fee, 5000 * 1.18, places=2)

    def test_roll_number_unique_constraint(self):
        with self.assertRaises(Exception):
            self.env['college.student'].create({
                'name': 'Duplicate',
                'roll_number': 'STU0001',
                'course_id': self.course.id
            })
