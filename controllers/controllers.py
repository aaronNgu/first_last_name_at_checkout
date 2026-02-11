# -*- coding: utf-8 -*-
# from odoo import http


# class FirstLastNameAtCheckout(http.Controller):
#     @http.route('/first_last_name_at_checkout/first_last_name_at_checkout', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/first_last_name_at_checkout/first_last_name_at_checkout/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('first_last_name_at_checkout.listing', {
#             'root': '/first_last_name_at_checkout/first_last_name_at_checkout',
#             'objects': http.request.env['first_last_name_at_checkout.first_last_name_at_checkout'].search([]),
#         })

#     @http.route('/first_last_name_at_checkout/first_last_name_at_checkout/objects/<model("first_last_name_at_checkout.first_last_name_at_checkout"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('first_last_name_at_checkout.object', {
#             'object': obj
#         })

