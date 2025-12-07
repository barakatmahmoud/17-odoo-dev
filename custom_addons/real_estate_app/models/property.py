from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'

    name = fields.Char(default='New')
    description = fields.Text()
    post_code = fields.Char(required=True)
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer(required=True)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage =fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])

    ### ADD SQL Constraints ###
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The property name must be unique!')
    ]

    ### ADD Logic or Python Validation ###
    @api.constrains('bedrooms')
    def _check_bedroom(self):
        for rec in self:
            if rec.bedrooms <=0:
                raise ValidationError("Please, Enter Valid Number Of Bedrooms")

