from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Property(models.Model):
    _name = 'property'
    ### ADD Chatter ###
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(default='New')
    ### ADD Sequence field ###
    ref = fields.Char(readonly=True, copy = False, default = lambda self: self.env['ir.sequence'].next_by_code('property_seq'))
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
    ### Create a field to get the creation time
    create_time = fields.Datetime(default=fields.Datetime.now())
    ### Field Time Compute
    next_time = fields.Datetime(compute='_compute_next_time')

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

    ### Calculate create time + 6 hours , use timedelta
    @api.depends('create_time')
    def _compute_next_time(self):
        for rec in self:
            if rec.create_time:
                rec.next_time = rec.create_time + timedelta(hours=6)
            else:
                rec.next_time = False

    ### ADD Button Action ###
    def draft_action(self):
        for rec in self:
            rec.create_property_history(rec.state, 'draft')
            rec.state = 'draft'

    def pending_action(self):
        for rec in self:
            rec.create_property_history(rec.state, 'pending')
            rec.state = 'pending'

    def sold_action(self):
        for rec in self:
            rec.create_property_history(rec.state, 'sold')
            rec.state = 'sold'
            ### USE message_post to send Message in Chatter ###
            rec.message_post(body="The Property has been Sold")

    def closed_action(self):
        for rec in self:
            rec.create_property_history(rec.state, 'closed')
            rec.state = 'closed'

    ### Overwrite write method and add logic Block edit when state == 'closed'
    # def write(self, vals):
    #     ### Block Edit in Specific State
    #     if self.filtered(lambda rec: rec.state == 'closed'):
    #         raise UserError("Cannot modify records in Close state.")
    #     return super().write(vals)

    def unlink(self):
        ### Block Delete in Specific State
        sold_property = self.filtered(lambda rec: rec.state == 'sold')
        if sold_property:
            for rec in sold_property:
                raise UserError(f"Cannot delete records in Sold state.{rec.name}")
        return super().unlink()

    ### Compute Method ###
    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price

    ### onchange Method ###
    # @api.onchange('expected_price')
    # def _onchange_expected_price(self):
    #     for rec in self:
    #         print("REC", rec)
    #         print('INSIDE ONCHANGE')
    #         return {
    #             'warning': {
    #                 'title': "Warning",
    #                 'message': "Negative Value",
    #             }
    #         }

    ### ADD Function Of Cron Job ###
    def check_expected_selling_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.date_expected and rec.date_expected < fields.date.today():
                rec.is_late = True

    ### Env Object ###
    def print_env_details(self):
        ### Print login user
        print(self.env.user)
        ### Print login user ID
        print(self.env.uid)
        ### print user company
        print(self.env.company)
        ### print env context
        print(self.env.context)
        ### Access any model
        partners = self.env['res.partner'].search([])
        print(partners)
        ### Print Lang
        print(self.env.context.get('lang'))
        ### If User Has Specific group
        # self.env.user.has_group('your_module.group_hr_manager')

    # def create(self, vals):
    #     res = super(Property, self).create(vals)
    #     ### ADD Sequence ###
    #     if res.ref == 'New':
    #         res.ref = self.env['ir.sequence'].next_by_code('property_seq')
    #     return res

    ### ADD Function to create record in another model when state change
    def create_property_history(self, old_state, new_state, reason="Default Value"):
        for rec in self:
            rec.env['property.history'].sudo().create({
                'user_id': rec.env.uid,
                'property_id': rec.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason or False,
                ### use Command tuples to create in one2many field
                'property_history_line_ids': [(0,0, {'description': line.description, 'area':line.area})for line in rec.property_line_ids]
            })

    ### Open Wizard through Server Action###
    def action_open_change_state_wizard(self):
        #Get Wizard Action
        action = self.env['ir.actions.actions']._for_xml_id('real_estate_app.change_state_wizard_action')
        #Add Context to Wizard action
        action['context'] = {'default_property_id': self.id}
        return action

    ### Action to smart btn To open Specific View
    def action_open_related_owner(self):
        action =  self.env['ir.actions.actions']._for_xml_id('real_estate_app.owner_action')
        print("Action>>>>", action)
        view_id = self.env.ref('real_estate_app.owner_form_view').id
        action['res_id'] = self.owner_id.id
        action['views'] = [[view_id, 'form']]
        return action

    ### ADD Method to Open URL Internal in odoo
    def action_open_partners(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/odoo/contacts?view_type=list',
            'target': 'self'
        }

### ADD Lines in Model ###
class PropertyLine(models.Model):
    _name = 'property.line'

    property_id = fields.Many2one('property', ondelete='cascade')
    area = fields.Float()
    description = fields.Char()
