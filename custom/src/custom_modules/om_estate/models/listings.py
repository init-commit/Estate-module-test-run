# model to show all the houses listed

from odoo import fields, api, models

class EstateListings(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = "estate.listings"
    _description = "All available listings for purchase and lease"


    realtor_id = fields.Many2one('estate.agent', string = "Realtor ID")
    # listing_date = fields.Date(string = "Listing date", default=fields.Date.context_today)
    listing_time = fields.Datetime(string = "Listing time", default=fields.Datetime.now)
    name = fields.Char(string="House Type")
    size_in_sq = fields.Float(string="Size in SQ")
    status = fields.Selection([('Available', 'Available'), ('Unavailable', 'Unavailable')], string='Status')
    purchase_value = fields.Float(string="Purchase Value")
    lease_value = fields.Float(string="Lease Value")
    phone = fields.Char(string='Phone')
    active = fields.Boolean(string="Active", default=True)

