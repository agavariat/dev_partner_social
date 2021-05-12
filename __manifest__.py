# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'Partner Social Links',
    'version': '12.0.1.0',
    'sequence': 1,
    'category': 'Sales',
    'description':
        """
        This Module add below functionality into odoo

        1.Allow you to set social networking links for contacts\n
        2.Contact social links are displayed on kanban view of contact as buttons\n
        3.You can navigate to contact's social profile by clicking on these buttons\n

Odoo partner account 
odoo social 
odoo social account
odoo facebook 
odoo instagram
odoo linkdin

    """,
    'summary': 'odoo app will add Social Networking links of contacts/partner',
    'depends': ['contacts'],
    'data': ['view/contact_view.xml'],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    # author and support Details =============#
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': 'devintelle@gmail.com',
    'price':10.0,
    'currency':'EUR',
    'live_test_url':'https://youtu.be/713HZhiJM2I',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
