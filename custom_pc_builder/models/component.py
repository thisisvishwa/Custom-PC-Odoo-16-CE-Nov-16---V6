```python
from odoo import models, fields

class Component(models.Model):
    _name = 'custom_pc_builder.component'
    _description = 'PC Component'

    name = fields.Char(string='Component Name', required=True)
    component_type = fields.Selection([
        ('cpu', 'CPU'),
        ('ram', 'RAM'),
        ('gpu', 'GPU'),
        ('storage', 'Storage'),
        ('peripheral', 'Peripheral'),
    ], string='Component Type', required=True)
    options = fields.Text(string='Options')
    price = fields.Float(string='Price', digits=(6, 2))
    image = fields.Binary(string='Image')
    description = fields.Text(string='Description')
```