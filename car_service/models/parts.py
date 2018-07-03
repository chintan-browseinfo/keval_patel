from odoo import fields,models,api, _




class parts(models.Model):
	_name="parts.add"
	_description="new parts"

	#def _init_(self)

	name=fields.Selection((('glass','glass'), ('engine','engine'),('wheel','wheel'),('head','head light')),
                                 string='select parts')
	price=fields.Char(string="price")

	garage_id=fields.Many2one('mech.details',string='garage')
	buy=fields.Boolean(string='want to buy')
	seller1=fields.Many2one('email.details',string='seller')
	#item=fields.Selection((('glass','glass'), ('engine','engine'),('wheel','wheel'),('head','head light')),
                   #string='select parts')
	email = fields.Char(related='seller1.email',string='email')
	phone = fields.Char(related='seller1.phone',string='phone')
	
	#want_buy=fields.Boolean(string='want to buy')
	#seller=fields.Many2one('res.partner',string='seller')
	#buy=fields.Char(string='Buy')
	#item=fields.Char(string='item to buy')


