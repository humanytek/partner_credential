from openerp import api, fields, models


class PartnerCredential(models.Model):
    _inherit = 'res.partner'

    identification_type = fields.Selection([
        ('ife', 'IFE'),
        ('pasaporte', 'Pasaporte'),
    ])
    identification_number = fields.Char()
    expiration_date = fields.Date()
    elector_key = fields.Char()
