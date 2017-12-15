# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import common

class test_sseLunch(common.TransactionCase):

    def setUp(self):
        """*****setUp*****"""
        super(test_sseLunch, self).setUp()

        self.lunchModule = self.env['lunch.order.line.favorite']

        self.demo_user = self.env['res.users'].search([('name', '=', 'Demo User')])
        
        self.product_bolognese_ref = self.env['ir.model.data'].get_object_reference('lunch', 'product_Bolognese')
        self.product_Bolognese_id = self.product_bolognese_ref and self.product_bolognese_ref[1] or False
        self.new_id_order = self.env['lunch.order'].create({
            'user_id': self.demo_user.id,
            'order_line_ids': '[]',
            })
        self.new_id_order_line1 = self.env['lunch.order.line'].create({
            'order_id': self.new_id_order.id,
            'product_id': self.product_Bolognese_id,
            'note': '+Emmental',
            'cashmove': [],
            'price': self.env['lunch.product'].browse(self.product_Bolognese_id).price,
            })


        self.product_steak_id = self.env['lunch.product'].search([('name', '=', "steak")]).id
        self.new_id_order = self.env['lunch.order'].create({
            'user_id': self.demo_user.id,
            'order_line_ids': '[]',
            })
        self.new_id_order_line2 = self.env['lunch.order.line'].create({
            'order_id': self.new_id_order.id,
            'product_id': self.product_steak_id,
            'note': '',
            'cashmove': [],
            'price': self.env['lunch.product'].browse(self.product_steak_id).price,
            })

        self.product_pasta_id = self.env['lunch.product'].search([('name', '=', "pasta")]).id
        self.new_id_order = self.env['lunch.order'].create({
            'user_id': self.demo_user.id,
            'order_line_ids': '[]',
            })
        self.new_id_order_line3 = self.env['lunch.order.line'].create({
            'order_id': self.new_id_order.id,
            'product_id': self.product_pasta_id,
            'note': '',
            'cashmove': [],
            'price': self.env['lunch.product'].browse(self.product_pasta_id).price,
            })
        

    def test_00_sse_lunch_order(self):
        self.order_one = self.new_id_order_line1
        self.order_one.order()
        self.order_two = self.new_id_order_line2
        self.order_two.order()
        self.order_three = self.new_id_order_line3
        self.order_three.order()

    def test_01_sse_lunch_order(self):
        self.test_00_sse_lunch_order()
        favoriteMenu = self.lunchModule.favorite_menus();
        print(favoriteMenu);


