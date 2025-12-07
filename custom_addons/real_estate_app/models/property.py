from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

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
    ### Many2one field ###
    owner_id = fields.Many2one('owner', string='Owner')
    ### Many2many field ###
    tag_ids = fields.Many2many('tag')
    ### state field to Do Workflow ###
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
    ], default='draft')

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

    ### ADD Button Action ###
    def draft_action(self):
        for rec in self:
            rec.state = 'draft'

    def pending_action(self):
        for rec in self:
            rec.state = 'pending'

    def sold_action(self):
        for rec in self:
            rec.state = 'sold'

    def write(self, vals):
        ### Block Edit in Specific State
        if self.filtered(lambda rec: rec.state == 'sold'):
            raise UserError("Cannot modify records in sold state.")
        return super().write(vals)

    def unlink(self):
        ### Block Delete in Specific State
        if self.filtered(lambda rec: rec.state == 'sold'):
            raise UserError("Cannot delete records in Sold state.")
        return super().unlink()

