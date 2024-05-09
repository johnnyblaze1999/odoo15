from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestHospitalAppointment(TransactionCase):

    def setUp(self):
        super(TestHospitalAppointment, self).setUp()
        self.patient = self.env['hospital.patient'].create({'name': 'Test Patient', 'age': 25, 'gender': 'male'})
        self.doctor = self.env['hospital.doctor'].create({'doctor_name': 'Test Doctor', 'age': 40, 'gender': 'male'})
        self.appointment = self.env['hospital.appointment'].create({'patient_id': self.patient.id, 'doctor_id': self.doctor.id})

    def test_appointment(self):
        # Check the creation of an appointment
        self.assertEqual(self.appointment.patient_id, self.patient, 'Appointment not created with correct patient')
        self.assertEqual(self.appointment.doctor_id, self.doctor, 'Appointment not created with correct doctor')

    def test_patient_age(self):
        # Check the patient's age
        self.assertEqual(self.patient.age, 25, 'Patient age not correctly set')

    def test_doctor_age(self):
        # Check the doctor's age
        self.assertEqual(self.doctor.age, 40, 'Doctor age not correctly set')

    def test_patient_gender(self):
        # Check the patient's gender
        self.assertEqual(self.patient.gender, 'male', 'Patient gender not correctly set')

    def test_doctor_gender(self):
        # Check the doctor's gender
        self.assertEqual(self.doctor.gender, 'male', 'Doctor gender not correctly set')