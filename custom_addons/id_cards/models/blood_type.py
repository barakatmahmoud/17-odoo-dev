import apt_inst
from odoo import models, fields

class BloodType(models.Model):
    _name = 'blood.type'

    name = fields.Char(required=True)
