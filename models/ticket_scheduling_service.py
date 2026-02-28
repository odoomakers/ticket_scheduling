from odoo import fields, models

class TicketSchedulingService(models.Model):
    _name = 'ticket.scheduling.service'
    _description = 'Ticket Scheduling Service'

    name = fields.Char("Name")
    description = fields.Char("Description")
    ticket_id = fields.Many2one("ticket.scheduling", "Ticket")
    is_published = fields.Boolean("Service Published")
    scheduled_tickets_ids = fields.One2many("scheduled.ticket", 'service_id', 'Scheduled Tickets')
    sequence = fields.Integer("Sequence")
