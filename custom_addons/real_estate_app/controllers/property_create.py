from odoo import http
from odoo.http import request

class PropertyCreate(http.Controller):

    # عرض الفورم
    @http.route('/property/create', type='http', auth='public', website=True)
    def create_property_form(self, **kwargs):
        return request.render('real_estate_app.create_property_template')

    # استقبال البيانات وعمل create
    @http.route('/property/submit', type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def submit_property(self, **post):
        request.env['property'].sudo().create({
            'name': post.get('name'),
            'description': post.get('description'),
            'expected_price': float(post.get('price')),
            'post_code': post.get('post_code'),
        })
        # redirect لصفحة success
        return request.redirect('/property/success')


    # صفحة النجاح
    @http.route('/property/success', type='http', auth='public', website=True)
    def property_success(self, **kwargs):
        return request.render('real_estate_app.property_success_template')