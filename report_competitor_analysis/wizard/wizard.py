from odoo import models, api, fields

from datetime import datetime



class DetailWizard(models.TransientModel):
    _name = "competitor.analysis.wizard"
    _description = "Competitor Analysis Wizard"
    # _inherit = 'pos.config'

    customer_name = fields.Many2one('res.partner',string="By Customer Name",)
    by_comp = fields.Char(string='By Competitiors')
    by_amount = fields.Char(string='By Amount')
    by_tender = fields.Char(string='By Tender No')
    by_status = fields.Char(string='By Status')
    by_quotation = fields.Char(string='By Quotation')
    by_date = fields.Date(string='By Date')
    by_price = fields.Char(string='By Price')
    by_items = fields.Char(string='By Items')

    def competitor_analysis_report(self):

        return self.env.ref('report_competitor_analysis.competitor_analysis_report').report_action(self)


