```python
from odoo import models, fields

class PcBuild(models.Model):
    _name = 'pc.build'
    _description = 'PC Build'

    name = fields.Char(string='Build Name', required=True)
    cpu_id = fields.Many2one('component', string='CPU', domain=[('component_type', '=', 'CPU')])
    ram_id = fields.Many2one('component', string='RAM', domain=[('component_type', '=', 'RAM')])
    gpu_id = fields.Many2one('component', string='GPU', domain=[('component_type', '=', 'GPU')])
    storage_id = fields.Many2one('component', string='Storage', domain=[('component_type', '=', 'Storage')])
    peripheral_ids = fields.Many2many('component', string='Peripherals', domain=[('component_type', '=', 'Peripheral')])

    def preview_build(self):
        # Method to preview the build
        pass

    def save_build(self):
        # Method to save the build
        pass

    def retrieve_build(self):
        # Method to retrieve the build
        pass
```