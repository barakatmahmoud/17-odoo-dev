from odoo import models, fields

### Class Extend inheritance ###
class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_owner = fields.Many2one('owner', string='Property Owner')