from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestProperty(TransactionCase):

    def setUp(self):
        super().setUp()

        # Create Owner (Many2one dependency)
        self.owner = self.env['owner'].create({
            'name': 'Test Owner',
            'phone': '0100000000',
        })

        # Create Property Record
        self.property = self.env['property'].create({
            'name': 'Test Property',
            'post_code': '12345',
            'bedrooms': 3,
            'expected_price': 100000,
            'selling_price': 80000,
            'owner_id': self.owner.id,
        })
    print("AFTER SETUP")

    def test_property_creation(self):
        self.assertTrue(self.property)
        self.assertEqual(self.property.name, 'Test Property')
        self.assertEqual(self.property.state, 'draft')
    print("AFTER CREATION")

    def test_unique_name_constraint(self):
        with self.assertRaises(Exception):
            self.env['property'].create({
                'name': 'Test Property',  # duplicate
                'post_code': '99999',
                'bedrooms': 2,
            })
    print("AFTER UNIQUE NAME CONSTRAINT")

    def test_bedrooms_constraint(self):
        with self.assertRaises(ValidationError):
            self.env['property'].create({
                'name': 'Invalid Property',
                'post_code': '11111',
                'bedrooms': 0,  # invalid
            })
    print("AFTER BEDROOMS CONSTRAINT")

    def test_diff_compute(self):
        self.assertEqual(self.property.diff, 20000)
    print("AFTER DIFF COMPUTE")

    def test_owner_phone_related(self):
        self.assertEqual(
            self.property.owner_phone,
            self.owner.phone
        )
    print("AFTER PHONE RELATED")

    def test_state_change(self):
        self.property.state = 'sold'
        self.assertEqual(self.property.state, 'sold')
    print("AFTER STATE_CHANGE")

    def test_sequence_generated(self):
        self.assertTrue(self.property.ref)
        self.assertNotEqual(self.property.ref, 'New')
    print("AFTER SEQUENCE GENERATED")