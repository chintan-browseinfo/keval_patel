from odoo import fields,models,api, _
from datetime import datetime, timedelta



class Customer(models.Model):

	_name="customer.details"
	_description="details of customer"



	@api.depends('Days')
	def _cal_date(self):
		for my in self:
			if not my.date1:
				return

			print "==========date==========",my.date1
			d1=datetime.strptime(my.date1,'%Y-%m-%d').date()
			print"==================d1====================="
			my.return_date=d1+timedelta(days=my.Days)




	@api.model
	def create(self,vals):
		cus_obj=self.env['customer.details']
		email_id=vals.get("phone",self.env.customer.details)
		
		
		
		








	name=fields.Char(string="customer name",required=True)
	phone=fields.Char(string="phone number",size=10,required=True)
	#car=fields.Selection((('h','Honda'), ('b','BMW'),('t','Tesla')),
                   #string='select car',required=True)
	city=fields.Selection((('a','Ahmedabad'), ('g','Goa'),('d','Delhi')),
                   string='select city',required=True)
	#service_type=fields.Many2one('mech.details',string="service")
	urgent=fields.Selection((('y','Yes'),('n','No')),string="urgent",required=True)
	
	Days=fields.Integer(string="Days takes")
	vehical=fields.Text(string="vehical problem")
	#customer_line=fields.One2many('service.details','customer_id',string="lines of customer")
	date1=fields.Date(string="date ")
	
	service=fields.Many2one('mech.details',string="service")
	return_date=fields.Date(string="expected return date",store=True, compute='_cal_date')
	aadhar_id=fields.Many2one('res.partner',string="partner")
	