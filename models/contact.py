# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class Contacts(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def open_instagram_link(self):
        if not self.instagram_link:
            raise ValidationError(_('''Please specify Instagram link first'''))
        return {'name': _("Instagram"),
                'type': 'ir.actions.act_url',
                'url': self.instagram_link,
                'target': 'new'
                }

    @api.multi
    def open_facebook_link(self):
        if not self.facebook_link:
            raise ValidationError(_('''Please specify Facebook link first'''))
        return {'name': _("Facebook"),
                'type': 'ir.actions.act_url',
                'url': self.facebook_link,
                'target': 'new'
                }

    @api.multi
    def open_linkedin_link(self):
        if not self.linkedin_link:
            raise ValidationError(_('''Please specify Linked In link first'''))
        return {'name': _("Linked In"),
                'type': 'ir.actions.act_url',
                'url': self.linkedin_link,
                'target': 'new'
                }

    @api.multi
    def open_youtube_link(self):
        if not self.youtube_link:
            raise ValidationError(_('''Please specify YouTube link first'''))
        return {'name': _("YouTube"),
                'type': 'ir.actions.act_url',
                'url': self.youtube_link,
                'target': 'new'
                }

    @api.multi
    def open_pinterest_link(self):
        if not self.pinterest_link:
            raise ValidationError(_('''Please specify Pinterest link first'''))
        return {'name': _("Pinterest"),
                'type': 'ir.actions.act_url',
                'url': self.pinterest_link,
                'target': 'new'
                }

    @api.multi
    def open_twitter_link(self):
        if not self.twitter_link:
            raise ValidationError(_('''Please specify Twitter link first'''))
        return {'name': _("Twitter"),
                'type': 'ir.actions.act_url',
                'url': self.twitter_link,
                'target': 'new'
                }

    linkedin_link = fields.Char(string='Linked In')
    youtube_link = fields.Char(string='Youtube')
    facebook_link = fields.Char(string='Facebook')
    instagram_link = fields.Char(string='Instagram')
    pinterest_link = fields.Char(string='Pinterest')
    twitter_link = fields.Char(string='Twitter')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: