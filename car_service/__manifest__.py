   # -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Car service',
    'version': '1.0',
    'category': 'serviceing',
    'sequence': 120,
    'summary': 'Sample Module for car serviceing',
    'description': """car servies Module
    """,
    'website': 'https://www.browseinfo.in',
    'depends': ['base', 'sale'],
    'data': ['views/customer_views.xml','views/mech_views.xml','views/parts.xml','views/tax.xml',
    'views/buy_parts.xml','views/sale_views.xml','views/email.xml','views/Aadhar.xml'],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
