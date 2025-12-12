from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Property(models.Model):
    _name = 'property'
    ### ADD Chatter ###
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(default='New')
    description = fields.Text()
    post_code = fields.Char(required=True, tracking=True)
    date_availability = fields.Date()
    date_expected = fields.Date()
    is_late = fields.Boolean(default=False)
    expected_price = fields.Float()
    selling_price = fields.Float()
    ### Compute Field ###
    diff = fields.Float(compute='_compute_diff', store=True)
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
        ('closed', 'Closed'),
    ], default='draft',tracking=True)
    ### Related Field ###
    owner_phone = fields.Char(related='owner_id.phone')
    ### ADD One2many Line ###
    property_line_ids = fields.One2many('property.line', 'property_id')

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
            ### USE message_post to send Message in Chatter ###
            rec.message_post(body="The Property has been Sold")

    def closed_action(self):
        for rec in self:
            rec.state = 'closed'

    def write(self, vals):
        ### Block Edit in Specific State
        if self.filtered(lambda rec: rec.state == 'closed'):
            raise UserError("Cannot modify records in Close state.")
        return super().write(vals)

    def unlink(self):
        ### Block Delete in Specific State
        if self.filtered(lambda rec: rec.state == 'sold'):
            raise UserError("Cannot delete records in Sold state.")
        return super().unlink()

    ### Compute Method ###
    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price

    ### onchange Method ###
    @api.onchange('expected_price')
    def _onchange_expected_price(self):
        for rec in self:
            print("REC", rec)
            print('INSIDE ONCHANGE')
            return {
                'warning': {
                    'title': "Warning",
                    'message': "Negative Value",
                }
            }

    ### ADD Function Of Cron Job ###
    def check_expected_selling_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.date_expected and rec.date_expected < fields.date.today():
                rec.is_late = True

### ADD Lines in Model ###
class PropertyLine(models.Model):
    _name = 'property.line'

    property_id = fields.Many2one('property', ondelete='cascade')
    area = fields.Float()
    description = fields.Char()
