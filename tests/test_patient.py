from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestPatient(TransactionCase):
    def setUp(self):
        super(TestPatient, self).setUp()
        self.patient = self.env['hospital.patient']

    def test_create_patient(self):
        patient = self.patient.create({
            'name': 'Test Patient',
            'age': 24,
            'gender': 'male',
            'note': 'This is a test note for test patient'
        })

        self.assertEqual(patient.name, 'Test Patient')
        self.assertEqual(patient.age, 24)
        self.assertEqual(patient.gender, 'male')
        self.assertEqual(patient.note, 'This is a test note for test patient')

    def test_create_patient_no_name(self):
        with self.assertRaises(ValidationError):
            self.patient.create({
                'age': 24,
                'gender': 'male',
                'note': 'This is a test note for test patient'
            })
    
    def test_create_patient_negative_age(self):
        with self.assertRaises(ValidationError):
            self.patient.create({
                'name': 'Test Patient',
                'age': -24,
                'gender': 'male',
                'note': 'This is a test note for test patient'
            })

    def test_create_patient_invalid_gender(self):
        with self.assertRaises(ValidationError):
            self.patient.create({
                'name': 'Test Patient',
                'age': 24,
                'gender': 'invalid',
                'note': 'This is a test note for test patient'
            })
