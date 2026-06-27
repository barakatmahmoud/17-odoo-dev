from odoo import models, fields


class ToDoList(models.Model):
    _name = 'to.do.list'
    _description = 'To Do List'

    name = fields.Char(
        string='Task',
        required=True,
    )

    completed = fields.Boolean(
        string='Completed',
        default=False,
    )

    color = fields.Char(
        string='Color',
    )