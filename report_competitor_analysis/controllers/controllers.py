# -*- coding: utf-8 -*-
# from odoo import http


# class ReportCompetitorAnalysis(http.Controller):
#     @http.route('/report_competitor_analysis/report_competitor_analysis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_competitor_analysis/report_competitor_analysis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_competitor_analysis.listing', {
#             'root': '/report_competitor_analysis/report_competitor_analysis',
#             'objects': http.request.env['report_competitor_analysis.report_competitor_analysis'].search([]),
#         })

#     @http.route('/report_competitor_analysis/report_competitor_analysis/objects/<model("report_competitor_analysis.report_competitor_analysis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_competitor_analysis.object', {
#             'object': obj
#         })
