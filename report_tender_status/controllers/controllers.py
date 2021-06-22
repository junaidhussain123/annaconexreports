# -*- coding: utf-8 -*-
# from odoo import http


# class ReportTenderStatus(http.Controller):
#     @http.route('/report_tender_status/report_tender_status/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_tender_status/report_tender_status/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_tender_status.listing', {
#             'root': '/report_tender_status/report_tender_status',
#             'objects': http.request.env['report_tender_status.report_tender_status'].search([]),
#         })

#     @http.route('/report_tender_status/report_tender_status/objects/<model("report_tender_status.report_tender_status"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_tender_status.object', {
#             'object': obj
#         })
