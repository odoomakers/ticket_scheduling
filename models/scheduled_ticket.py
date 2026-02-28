from odoo import fields, models


class ScheduledTicket(models.Model):
    _name = 'scheduled.ticket'
    _description = 'Scheduled Ticket'

    name = fields.Char("Name")
    client_id = fields.Many2one("res.partner")
    status = fields.Selection([
        ('draft', 'Drfat'),('open', 'Open'),('scheduling', 'Scheduling'),
        ('closed', 'Closed'),('cancelled','Cancelled')
    ])
    start_datetime = fields.Datetime('Start Time')
    end_datetime = fields.Datetime("End Time")