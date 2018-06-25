from odoo import fields,models,api, _




class parts(models.Model):
	_name='parts.add'
	_description="new parts"


	name=fields.Selection((('glass','glass'), ('engine','engine'),('wheel','wheel'),('head','head light')),
                   string='select parts',required=True)

	garage_id=fields.Many2one('mech.details',string='garage')