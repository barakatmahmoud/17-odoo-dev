from odoo import http
from odoo.http import request
import base64

class IDCardsRequest(http.Controller):

    # عرض الفورم
    @http.route('/id/cards/create', type='http', auth='public', website=True)
    def create_id_cards(self, **kwargs):
        countries = request.env['res.country'].sudo().search([])
        blood_types = request.env['blood.type'].sudo().search([])
        return request.render('id_cards.id_cards_request_template',{
            'countries': countries,
            'blood_types': blood_types,
        })

    # استقبال البيانات وعمل create
    @http.route('/id/cards/submit', type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def submit_property(self, **kwargs):
        print("KWARGS>>", kwargs)
        attachment = request.httprequest.files.get('attachment')
        print("ATTACHMENT>>", attachment)
        attachment_data = False
        if attachment:
            attachment_data = base64.b64encode(attachment.read())
            print("ATTACHMENT_DATA>>", attachment_data)

        request.env['id.cards.request'].sudo().create({
            'name': kwargs.get('name'),
            'id_number': kwargs.get('id_number'),
            'phone_number': kwargs.get('phone_number'),
            'email': kwargs.get('email'),
            'country_id': kwargs.get('country_id'),
            'city_id': kwargs.get('city_id'),
            'address': kwargs.get('address'),
            'date': kwargs.get('date'),
            'blood_type_id': kwargs.get('blood_type'),
            'attachment': attachment_data,
            'attachment_name': attachment.filename,

        })
        # redirect لصفحة success
        return request.redirect('/id/cards/success')


    # صفحة النجاح
    @http.route('/id/cards/success', type='http', auth='public', website=True)
    def id_cards_success(self, **kwargs):
        return request.render('id_cards.id_cards_success_template')

    @http.route('/get/cities',type='json',auth='public',website=True)
    def get_cities(self, country_id):
        cities = request.env['res.country.state'].sudo().search([('country_id', '=', int(country_id))])
        return [
            {
                'id': city.id,
                'name': city.name,
            }
            for city in cities
        ]