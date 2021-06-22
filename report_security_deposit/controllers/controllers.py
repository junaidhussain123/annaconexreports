# -*- coding: utf-8 -*-
# from odoo import http


# class ReportSecurityDeposit(http.Controller):
#     @http.route('/report_security_deposit/report_security_deposit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_security_deposit/report_security_deposit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_security_deposit.listing', {
#             'root': '/report_security_deposit/report_security_deposit',
#             'objects': http.request.env['report_security_deposit.report_security_deposit'].search([]),
#         })

#     @http.route('/report_security_deposit/report_security_deposit/objects/<model("report_security_deposit.report_security_deposit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_security_deposit.object', {
#             'object': obj
#         })
