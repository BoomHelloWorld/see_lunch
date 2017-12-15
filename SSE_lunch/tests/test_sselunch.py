# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import common

class test_sseLunch(common.TransactionCase):

    def setUp(self):
        """*****setUp*****"""
        super(test_sseLunch, self).setUp()

        self.lunchModule = self.env['lunch.order.line.favorite']
        self.lunchMainModule = self.env['lunch.order']

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
        

    def order1(self):
        self.lunchMainModule.create({
            'product_id': self.env['lunch.product'].search([('name', '=', "steak")]).id ,
            'order_id': self.new_id_order.id})
        self.lunchMainModule.order()

    def order2(self):
        self.lunchMainModule.create({
            'product_id': self.env['lunch.product'].search([('name', '=', "chickenWing")]).id ,
            'order_id': self.new_id_order.id})
        self.lunchMainModule.order()

    def order3(self):
        self.lunchMainModule.create({
            'product_id': self.env['lunch.product'].search([('name', '=', "pasta")]).id ,
            'order_id': self.new_id_order.id})
        self.lunchMainModule.order()

    def order4(self):
        self.lunchMainModule.create({
            'product_id': self.env['lunch.product'].search([('name', '=', "chickenLeg")]).id ,
            'order_id': self.new_id_order.id})
        self.lunchMainModule.order()



    def test_00_sse_lunch_order(self):
        self.lunchMainModule.create({
            'product_id': self.env['lunch.product'].search([('name', '=', "chickenWing")]).id ,
            'order_id': self.new_id_order.id})
        self.lunchMainModule.order()

    def test_11_sse_lunch_order(self):
        self.order1()
        favoriteMenu = self.lunchModule.favorite_menus();
        print(favoriteMenu)

    def test_12_sse_lunch_order(self):
        self.order1()
        self.order1()
        self.order1()
        self.order1()

        self.order2()
        self.order2()
        self.order2()

        self.order3()

        favoriteMenu = self.lunchModule.favorite_menus();
        print(favoriteMenu)

    def test_13_sse_lunch_order(self):
        self.order1()
        self.order1()
        self.order1()
        self.order1()

        self.order2()
        self.order2()
        self.order2()

        self.order3()

        self.order4()
        self.order4()

        favoriteMenu = self.lunchModule.favorite_menus();
        print(favoriteMenu)

    def test_14_sse_lunch_order(self):
        self.order1()
        self.order1()

        self.order2()
        self.order2()

        self.order3()
        self.order3()

        self.order4()
        self.order4()

        favoriteMenu = self.lunchModule.favorite_menus();
        print(favoriteMenu)


