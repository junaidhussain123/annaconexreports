from odoo import models, api, fields

from datetime import datetime



class DetailWizard(models.TransientModel):
    _name = "tender.status.wizard"
    _description = "Tender Status Wizard"
    # _inherit = 'pos.config'

    customer_name = fields.Many2one('res.partner',string="By Customer Name",)
    by_tender_name = fields.Char(string='By Tender No')
    by_month = fields.Char(string='By Month')

    total_value = fields.Char(string='By Total Value')
    earnest_money = fields.Char(string='By Earnest Money')
    by_status = fields.Char(string='By Status')
    by_quotation = fields.Char(string='By Quotations')
    date_opening = fields.Date(string='By Date of Opening')

    def tender_status_report(self):

        return self.env.ref('report_tender_status.tender_status_report').report_action(self)


