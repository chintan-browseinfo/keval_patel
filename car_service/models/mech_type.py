from odoo import fields,models,api, _


class mech(models.Model):
	
	_name="mech.details"
	_description="details of Mechanic" 




	name=fields.Selection((('Servicing','Servicing'), ('Reparing','Reparing'),('Washing','Washing'),('Painting','Painting')),
                   string='select Servicing',required=True)
	
	Mechanic=fields.Many2one('res.partner',string="Mechanic")
	vehical=fields.Selection((('c','4 wheeler'),('b','2 wheeler')),required=True)
	date=fields.Date(string="order date")
	damage=fields.Boolean(string="damage")
	parts = fields.One2many('parts.add','garage_id',String="add parts to replase")
	garage_ids=fields.Many2many('tax.details','tax_garage_rel','garage_id','tax_id',string='tax',required=True,copy=False)
	
	#sevice_id=fields.Many2one('service.details',string='sevice_id')
	#tax_ids=fields.Many2many('service.details','service_mech_rel','tax_id','service_id',string='tax')
	#name=fields.Char(string=' Mechanic',required=True)
	#phone=fields.Char(string="Phone number",required=True,size=10)
	#city=fields.Selection((('a','Ahmedabad'), ('g','Goa'),('d','Delhi')),
                   #string='select city',required=True)
	
	#service_id=fields.One2many('customer.details','service_type',string="service_id")
	#experiance=fields.Integer(string="Experiance",required=True)

