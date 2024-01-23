from odoo import api,fields,models


class HorseDetails (models.Model):
    _name = "horse.details"
    _description = "Horse details"

    name = fields.Char(string='Name')
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")