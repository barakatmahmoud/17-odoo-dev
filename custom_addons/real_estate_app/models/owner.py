import apt_inst
from odoo import models, fields, api

class Owner(models.Model):
    _name = 'owner'

    name = fields.Char(required=True)
    address = fields.Char()
    phone = fields.Char()
    property_ids = fields.One2many('property', 'owner_id', string='Property', readonly=True)
    property_count = fields.Integer(compute='_compute_property_count')

    ### Calc Number of Smart Btn
    @api.depends('property_ids')
    def _compute_property_count(self):
        for rec in self:
            total = self.env['property'].sudo().search_count([('owner_id', '=', rec.id)])
            print("Total >>>", total)
            rec.property_count = total


    ### Open All property related whit Owner
    def action_view_property(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Property',
            'res_model': 'property',
            'view_mode': 'tree,form',
            'domain': [('owner_id', '=', self.id)],
            }



