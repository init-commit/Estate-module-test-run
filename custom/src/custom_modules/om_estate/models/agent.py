
from odoo import api, fields, models # type: ignore #

class EstateAgent(models.Model):
    _name = 'estate.agent'  # name of the table to be created 
    _description = 'Estate Agent'
    
    # Fields are column names
    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    phone = fields.Char(string='Phone')


# time to add out menus, view from the xml files
#  all xml files must be in views folder
