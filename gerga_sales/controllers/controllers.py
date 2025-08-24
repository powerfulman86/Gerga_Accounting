# -*- coding: utf-8 -*-
# from odoo import http


# class GergaSales(http.Controller):
#     @http.route('/gerga_sales/gerga_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gerga_sales/gerga_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gerga_sales.listing', {
#             'root': '/gerga_sales/gerga_sales',
#             'objects': http.request.env['gerga_sales.gerga_sales'].search([]),
#         })

#     @http.route('/gerga_sales/gerga_sales/objects/<model("gerga_sales.gerga_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gerga_sales.object', {
#             'object': obj
#         })
