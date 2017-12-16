# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import common

class test_sseLunch(common.TransactionCase):

    def setUp(self):
        """*****setUp*****"""
        super(test_sseLunch, self).setUp()

        self.demo_user = self.env['res.users'].search([('name', '=', 'Administrator')])
        
        self.new_id_order = self.env['lunch.order'].create({
            'user_id': self.demo_user.id,
            'order_line_ids': '[]',
            })

    def order1(self):
        self.product_cw_id = self.env['lunch.product'].search([('name', '=', "chickenWing")]).id
        self.new_id_order_line1 = self.env['lunch.order.line'].create({
            'order_id': self.new_id_order.id,
            'product_id': self.product_cw_id,
            })

    def order2(self):
        self.product_steak_id = self.env['lunch.product'].search([('name', '=', "steak")]).id
        self.new_id_order_line2 = self.env['lunch.order.line'].create({
            'order_id': self.new_id_order.id,
            'product_id': self.product_steak_id,
            })

    def order3(self):
        self.product_pasta_id = self.env['lunch.product'].search([('name', '=', "pasta")]).id
        self.new_id_order_line3 = self.env['lunch.order.line'].create({
            'order_id': self.new_id_order.id,
            'product_id': self.product_pasta_id,
            })

    def order4(self):
        self.product_cl_id = self.env['lunch.product'].search([('name', '=', "chickenLeg")]).id
        self.new_id_order_line4 = self.env['lunch.order.line'].create({
            'order_id': self.new_id_order.id,
            'product_id': self.product_cl_id,
            })



    def test_00_sse_lunch_order(self):
        self.product_cw_id = self.env['lunch.product'].search([('name', '=', "chickenWing")]).id
        self.new_id_order_line1 = self.env['lunch.order.line'].create({
            'order_id': self.new_id_order.id,
            'product_id': self.product_cw_id,
            })
        self.new_id_order_line1.confirm()

    def test_11_sse_lunch_order(self):
        """Add chickenWing(1) check result of favorite menu"""
        self.order1()
        favoriteMenu = self.env['lunch.order.line.favorite'].favorite_menus()
        print(favoriteMenu)
        self.assertEqual(self.env['lunch.order.line.favorite'].favorite_menus(), [('id', 'in', [[15]])])

    def test_12_sse_lunch_order(self):
        """Add chickenWing(4) steak(2) pasta(1) check result of favorite menu"""
        self.order1()
        self.order1()
        self.order1()
        self.order1()

        self.order2()
        self.order2()
        self.order2()

        self.order3()

        favoriteMenu = self.env['lunch.order.line.favorite'].favorite_menus()
        print(favoriteMenu)
        self.assertEqual(self.env['lunch.order.line.favorite'].favorite_menus(), [('id', 'in', [[15], [13], [16]])])

    def test_13_sse_lunch_order(self):
        """Add chickenWing(4) steak(2) pasta(1) chickenLeg(2) check result of favorite menu"""
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

        favoriteMenu = self.env['lunch.order.line.favorite'].favorite_menus()
        print(favoriteMenu)
        self.assertEqual(self.env['lunch.order.line.favorite'].favorite_menus(), [('id', 'in', [[15], [13], [14]])])

    def test_14_sse_lunch_order(self):
        """Add chickenWing(2) steak(2) pasta(2) chickenLeg(2) check result of favorite menu"""
        self.order1()
        self.order1()

        self.order2()
        self.order2()

        self.order3()
        self.order3()

        self.order4()
        self.order4()

        favoriteMenu = self.env['lunch.order.line.favorite'].favorite_menus()
        print(favoriteMenu)
        self.assertEqual(self.env['lunch.order.line.favorite'].favorite_menus(), [('id', 'in', [[16], [14], [13]])])


