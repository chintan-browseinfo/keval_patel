from odoo import fields,models,api, _
from odoo.exceptions import UserError


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


	@api.model
	def create(self,vals):
		print "==================================================",vals

		#if vals.get('name', _('New')) == _('New'):
		'''	if vehical in vals:

				if vehical==b:
					vals.update({'vehical':'b'})
				else :
					vals.update({'vehical':'c'})'''
		if vals.get('name')=='Washing' or vals.get('name')=='Painting' and vals.get('damage')==True:
				
			raise UserError(_('Please select service or Reparing if damage'))



		fields=self.env['mech.details'].search([('name','=','Servicing')])
		print "=================fffffffffffffffffffffff===========",fields


		'''if vals.get('name', _('New')) == _('New'):
		 	if damage in vals:
		 		if damage==True:
		 			vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['damage']).next_by_code('mech.details') or _('New')
		 		else:
		 			 vals['name'] = self.env['ir.sequence'].next_by_code('mech.details') or _('New')'''
		result = super(mech, self).create(vals)
		print "====================================",vals
		return result


	@api.multi
	def write(self,vals):
		print "=======================write===========================================",vals
		if vals.get('name')=='Washing' or vals.get('name')=='Painting' and vals.get('damage')==True:
				
			raise UserError(_('Please select service or Reparing if damage'))



		result = super(mech, self).write(vals)
		print "================write====================",result
		return result



		
		