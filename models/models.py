# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LunchOrderLineSendEmail(models.Model):
    _inherit = 'lunch.order.line'
    _name = 'lunch.order.line'
    email = fields.Char(related='supplier.email');
    user_information = fields.Many2one('res.partner',related='user_id.partner_id');
    
    @api.one
    def send_email(self):       
        templat = self.env['mail.template'].search([('name','=','LunchOrderLine')])
        for tpl in templat:
            tpl.send_mail(self.id,True,True,None)            

        
    @api.one
    def confirm(self):
        """
        confirm one or more order line, update order status and create new cashmove
        """        
        if self.user_has_groups("lunch.group_lunch_manager"):
            super(LunchOrderLineSendEmail,self).confirm();
            self.send_email();
        else:
            raise AccessError(_("Only your lunch manager sets the orders as received."))