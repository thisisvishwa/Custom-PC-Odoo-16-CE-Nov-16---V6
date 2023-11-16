```python
from odoo.tests import common

class TestComponent(common.TransactionCase):

    def setUp(self):
        super(TestComponent, self).setUp()
        self.Component = self.env['component']

    def test_create_component(self):
        """
        Test the creation of a component
        """
        component = self.Component.create({
            'name': 'Test Component',
            'type': 'CPU',
            'price': 200.00,
        })

        self.assertEqual(component.name, 'Test Component')
        self.assertEqual(component.type, 'CPU')
        self.assertEqual(component.price, 200.00)

    def test_update_component(self):
        """
        Test the update of a component
        """
        component = self.Component.create({
            'name': 'Test Component',
            'type': 'CPU',
            'price': 200.00,
        })

        component.write({
            'name': 'Updated Component',
            'price': 250.00,
        })

        self.assertEqual(component.name, 'Updated Component')
        self.assertEqual(component.price, 250.00)

    def test_delete_component(self):
        """
        Test the deletion of a component
        """
        component = self.Component.create({
            'name': 'Test Component',
            'type': 'CPU',
            'price': 200.00,
        })

        component.unlink()

        self.assertEqual(len(self.Component.search([('name', '=', 'Test Component')])), 0)
```