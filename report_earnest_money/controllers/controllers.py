# -*- coding: utf-8 -*-
# from odoo import http


# class ReportEarnestMoney(http.Controller):
#     @http.route('/report_earnest_money/report_earnest_money/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_earnest_money/report_earnest_money/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_earnest_money.listing', {
#             'root': '/report_earnest_money/report_earnest_money',
#             'objects': http.request.env['report_earnest_money.report_earnest_money'].search([]),
#         })

#     @http.route('/report_earnest_money/report_earnest_money/objects/<model("report_earnest_money.report_earnest_money"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_earnest_money.object', {
#             'object': obj
#         })
