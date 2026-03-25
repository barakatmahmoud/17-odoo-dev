from odoo import http
from odoo.http import request

class PropertyInfoPage(http.Controller):
    @http.route(['/property/info'], type='http', auth="public", website=True)
    def property_info(self, **kw):
        properties = request.env['property'].sudo().search([])
        return request.render('real_estate_app.property_info',{
            'properties': properties,
        })

