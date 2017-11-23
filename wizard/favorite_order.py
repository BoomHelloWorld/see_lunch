import random

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from collections import Counter


class LunchOrderLineFavorite(models.TransientModel):
	_name = 'lunch.order.line.favorite'

	@api.multi
	def favorite_menus(self):
		last_order_obj = self.env['lunch.order.line'].search([('user_id', '=', self.env.uid), ('product_id.active', '!=', False)], order='id desc')
		count_favorite = []

		for previous_order in last_order_obj:
			count_favorite.append(previous_order.name) 
			print previous_order.name

		word_counter = {}

		for word in count_favorite:
			if word in word_counter:
				word_counter[word] += 1
			else:
				word_counter[word] = 1

		popular_words = sorted(word_counter, key = word_counter.get, reverse = True)

		popular_ids1 = self.env['lunch.product'].search([('name', '=', popular_words[0:1])]).ids
		popular_ids2 = self.env['lunch.product'].search([('name', '=', popular_words[1:2])]).ids
		popular_ids3 = self.env['lunch.product'].search([('name', '=', popular_words[2:3])]).ids
		
		return [('id', 'in', [popular_ids1,popular_ids2,popular_ids3])]

	menu = fields.Many2many('lunch.product', domain=lambda self:self.favorite_menus())	
	@api.multi
	def favorite_pick(self):
		self.ensure_one()

		order_line = self.env['lunch.order.line'].create({
			'product_id': self.env['lunch.product'].search([('name', '=', self.menu.name)]).id ,
			'order_id': self._context['active_id']
		})
# end add







