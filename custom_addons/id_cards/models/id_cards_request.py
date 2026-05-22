import apt_inst
from odoo import models, fields

class IdCardsRequest(models.Model):
    _name = 'id.cards.request'

    name = fields.Char(required=True, readonly=True)
    id_number = fields.Char(required=True, readonly=True)
    phone_number = fields.Char(required=True, readonly=True)
    email = fields.Char(required=True, readonly=True)
    country_id = fields.Many2one('res.country', string='Country', required=True, readonly=True)
    city_id = fields.Many2one('res.country.state', string='City', required=True, readonly=True)
    address = fields.Char(readonly=True)
    date = fields.Date(required=True, readonly=True)
    attachment = fields.Binary(required=True, readonly=True)
    attachment_name = fields.Char(readonly=True)
    blood_type_id = fields.Many2one('blood.type', required=True, readonly=True)