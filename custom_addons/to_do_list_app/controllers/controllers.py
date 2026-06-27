# -*- coding: utf-8 -*-
# from odoo import http


# class ToDoListApp(http.Controller):
#     @http.route('/to_do_list_app/to_do_list_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/to_do_list_app/to_do_list_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('to_do_list_app.listing', {
#             'root': '/to_do_list_app/to_do_list_app',
#             'objects': http.request.env['to_do_list_app.to_do_list_app'].search([]),
#         })

#     @http.route('/to_do_list_app/to_do_list_app/objects/<model("to_do_list_app.to_do_list_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('to_do_list_app.object', {
#             'object': obj
#         })

