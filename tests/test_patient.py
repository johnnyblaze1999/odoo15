from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestPatient(TransactionCase):
    def setUp(self):
        super(TestPatient, self).setUp()
        self.patient = self.env['hospital.patient']

    # Test for patient creation
    def test_create_patient(self):
        patient = self.patient.create({'name': 'John Bread', 'age': 24, 'gender': 'male', 'note': 'This is a test note for test patient'
        })

        self.assertEqual(patient.name, 'John Bread')
        self.assertEqual(patient.age, 24)
        self.assertEqual(patient.gender, 'male')
        self.assertEqual(patient.note, 'This is a test note for test patient')

    # Test for missing input (patient's name)
    def test_patient_no_name(self):
        with self.assertRaises(ValidationError):
            self.patient.create({'age': 24, 'gender': 'male'
            })
    
    # Test for invalid input (negative age)
    def test_patient_negative_age(self):
        with self.assertRaises(ValidationError):
            self.patient.create({'name': 'John Bread', 'age': -24, 'gender': 'male',
            })

    # Test for the search functionality
    def test_patient_search(self):
        Patient1 = self.patient.create({'name': 'John Bread', 'age': 30})
        Patient2 = self.patient.create({'name': 'Jane Bread', 'age': 40})
        Patients = self.patient.search([('age', '>', 35)])

        self.assertEqual(Patients, Patient1)