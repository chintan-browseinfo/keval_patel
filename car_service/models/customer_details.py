from odoo import fields,models,api, _




class Customer(models.Model):
	_name="customer.details"
	_description="details of customer" 

	name=fields.Char(string="customer name",required=True)
	phone=fields.Char(string="phone number",size=10,required=True)
	#car=fields.Selection((('h','Honda'), ('b','BMW'),('t','Tesla')),
                   #string='select car',required=True)
	city=fields.Selection((('a','Ahmedabad'), ('g','Goa'),('d','Delhi')),
                   string='select city',required=True)
	#service_type=fields.Many2one('mech.details',string="service")
	urgent=fields.Selection((('y','Yes'),('n','No')),string="urgent",required=True)
	vehical=fields.Text(string="vehical problem")
	#customer_line=fields.One2many('service.details','customer_id',string="lines of customer")
	date=fields.Datetime(string="date and time")
	
	service=fields.Many2one('mech.details',string="service")