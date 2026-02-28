from odoo import fields, models


class TicketScheduling(models.Model):
    _name = 'ticket.scheduling'
    _description = 'Ticket Scheduling'

    name = fields.Char("Name")
    description = fields.Char("Description")
    service_ids = fields.One2many('ticket.scheduling.service', 'ticket_id', 'Service')
    tag_ids = fields.Many2many("crm.tags", 'Tags')
    email = fields.Char("Email")
    company_id = fields.Many2one("res.partner", 'Company')
