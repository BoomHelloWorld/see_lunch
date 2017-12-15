# -*- coding: utf-8 -*-
from odoo import http

# class SseLunch(http.Controller):
#     @http.route('/sse_lunch/sse_lunch/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sse_lunch/sse_lunch/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sse_lunch.listing', {
#             'root': '/sse_lunch/sse_lunch',
#             'objects': http.request.env['sse_lunch.sse_lunch'].search([]),
#         })

#     @http.route('/sse_lunch/sse_lunch/objects/<model("sse_lunch.sse_lunch"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sse_lunch.object', {
#             'object': obj
#         })