from odoo.tests.common import TransactionCase

class TestHospitalDoctor(TransactionCase):

    def setUp(self):
        super(TestHospitalDoctor, self).setUp()
        self.doctor = self.env['hospital.doctor']

    def test_doctor_creation(self):
        "Test Doctors are being created successfully"
        Doctor1 = self.doctor.create({'doctor_name': 'Doctor 1', 'gender': 'male', 'note': 'Cardiology'})

        # Check if the doctor was created
        self.assertEqual(len(self.doctor.search([])), 1)

        # Check if the doctor's doctor_name and note were correctly set
        self.assertEqual(Doctor1.doctor_name, 'Doctor 1')
        self.assertEqual(Doctor1.note, 'Cardiology')

    def test_doctor_update(self):
        "Test Doctors are being updated successfully"
        Doctor1 = self.doctor.create({'doctor_name': 'Doctor 1', 'note': 'Cardiology'})
        Doctor1.write({'doctor_name': 'Doctor 2', 'note': 'Neurology'})

        # Check if the doctor's doctor_name and note were correctly updated
        self.assertEqual(Doctor1.doctor_name, 'Doctor 2', 'Doctor names are mismatched')
        self.assertEqual(Doctor1.note, 'Neurology', 'Notes are mismatched')

    def test_doctor_deletion(self):
        "Test Doctors are being deleted successfully"
        Doctor1 = self.doctor.create({'doctor_name': 'Doctor 1', 'note': 'Cardiology'})
        Doctor1.unlink()

        # Check if the doctor was deleted
        self.assertEqual(len(self.doctor.search([])), 0, 'Error in deletion')

    def test_doctor_search(self):
        "Test Doctors are being searched successfully"
        Doctor1 = self.doctor.create({'doctor_name': 'Doctor 1', 'note': 'Cardiology'})
        Doctor2 = self.doctor.create({'doctor_name': 'Doctor 2', 'note': 'Neurology'})
        Doctors = self.doctor.search([('note', '=', 'Neurology')])

        # Check if the search returned the correct doctor
        self.assertEqual(Doctors, Doctor2, 'Cannot lookup the correct doctor')

    def test_doctor_count(self):
        "Test the count of Doctors is correct"
        Doctor1 = self.doctor.create({'doctor_name': 'Doctor 1', 'note': 'Cardiology'})
        Doctor2 = self.doctor.create({'doctor_name': 'Doctor 2', 'note': 'Neurology'})

        # Check if the count of doctors is correct
        self.assertEqual(len(self.doctor.search([])), 2, 'Cannot count the number of doctors')
