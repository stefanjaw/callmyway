# -*- coding: utf-8 -*-
# from odoo import http


# class Callmyway(http.Controller):
#     @http.route('/callmyway/callmyway/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/callmyway/callmyway/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('callmyway.listing', {
#             'root': '/callmyway/callmyway',
#             'objects': http.request.env['callmyway.callmyway'].search([]),
#         })

#     @http.route('/callmyway/callmyway/objects/<model("callmyway.callmyway"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('callmyway.object', {
#             'object': obj
#         })
