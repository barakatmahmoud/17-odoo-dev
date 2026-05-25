import apt_inst
from odoo import models, fields, api

class IdCardsRequest(models.Model):
    _name = 'id.cards.request'

    name = fields.Char(required=True, readonly=True)
    id_number = fields.Char(required=True, readonly=True)
    phone_number = fields.Char(required=True, readonly=True)
    email = fields.Char(required=True, readonly=True)
    country_id = fields.Many2one('res.country', string='Country', required=True, readonly=True)
    city_id = fields.Many2one('res.country.state', string='City', readonly=True)
    address = fields.Char(readonly=True)
    date = fields.Date(required=True, readonly=True)
    attachment = fields.Binary(required=True, readonly=True)
    attachment_name = fields.Char(readonly=True)
    blood_type_id = fields.Many2one('blood.type', required=True, readonly=True)

    ## Add map fields
    latitude = fields.Float(digits=(10, 7))
    longitude = fields.Float(digits=(10, 7))
    long_lat_map = fields.Html(readonly=True, compute='_compute_long_lat_map', sanitize=False)

    @api.depends('latitude', 'longitude')
    def _compute_long_lat_map(self):
        for rec in self:
            if rec.latitude and rec.longitude:
                lat = rec.latitude
                lon = rec.longitude
                delta = 0.01  # padding حوالين النقطة
                bbox = f"{lon - delta},{lat - delta},{lon + delta},{lat + delta}"
                src = (
                    f"https://www.openstreetmap.org/export/embed.html"
                    f"?bbox={bbox}&layer=mapnik&marker={lat},{lon}"
                )
                rec.long_lat_map = (
                    f'<iframe src="{src}" '
                    f'style="width:100%;height:450px;border:1px solid #ccc;border-radius:8px;" '
                    f'frameborder="0" scrolling="yes"></iframe>'
                )
            else:
                rec.long_lat_map = '<p class="text-muted">لم يتم تحديد الموقع بعد</p>'