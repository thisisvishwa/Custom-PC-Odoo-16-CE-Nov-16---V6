```python
from odoo import http
from odoo.http import request

class CustomPCBuilder(http.Controller):

    @http.route('/pc_builder', type='http', auth='user', website=True)
    def pc_builder(self, **kwargs):
        components = request.env['custom_pc_builder.component'].search([])
        return request.render('custom_pc_builder.pc_build_view', {
            'components': components
        })

    @http.route('/pc_builder/preview', type='http', auth='user', website=True)
    def pc_builder_preview(self, **kwargs):
        pc_build = request.env['custom_pc_builder.pc_build'].browse(int(kwargs.get('id')))
        return request.render('custom_pc_builder.pc_build_preview', {
            'pc_build': pc_build
        })

    @http.route('/pc_builder/save', type='json', auth='user', website=True)
    def pc_builder_save(self, **kwargs):
        pc_build = request.env['custom_pc_builder.pc_build'].create(kwargs)
        return {'status': 'success', 'message': 'PC Build saved successfully', 'pc_build_id': pc_build.id}

    @http.route('/pc_builder/retrieve', type='http', auth='user', website=True)
    def pc_builder_retrieve(self, **kwargs):
        pc_build = request.env['custom_pc_builder.pc_build'].browse(int(kwargs.get('id')))
        return request.render('custom_pc_builder.pc_build_view', {
            'pc_build': pc_build
        })
```