from odoo import models, fields


class PropertyHistory(models.Model):
    _name = 'property.history'

    user_id = fields.Many2one('res.users')
    property_id = fields.Many2one('property')
    old_state = fields.Char()
    new_state = fields.Char()
    reason = fields.Char()
    property_history_line_ids = fields.One2many('property.history.line', 'property_history_id')


class PrpHistoryLine(models.Model):
    _name = 'property.history.line'

    property_history_id = fields.Many2one('property.history')
    area = fields.Float()
    description = fields.Char()