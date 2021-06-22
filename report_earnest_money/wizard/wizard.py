from odoo import models, api, fields

from datetime import datetime



class DetailWizard(models.TransientModel):
    _name = "earnest.money.wizard"
    _description = "Earnest Money Wizard"
    # _inherit = 'pos.config'

    customer_name = fields.Many2one('res.partner',string="By Customer Name",)
    by_date_making=fields.Date(string="By Date Of Making")
    by_tender_name = fields.Char(string='By Tender No in case of Earnest Money')
    sale_order_num = fields.Char(string='By LOI No or Sale Order No in case of Security Deposit')
    by_closing_date = fields.Datetime(string='By Closing Date & Time')
    by_instrument_no = fields.Char(string='By Instrument No')
    by_favour_of = fields.Char(string='By Favour Of')
    by_cheque_no = fields.Char(string='By Cheque No')
    by_bank = fields.Char(string='By Bank')
    by_voucher_type = fields.Char(string='By Voucher Type')
    by_amount = fields.Char(string='By Amount')
    by_pending_amount = fields.Char('By Pending Amount')
    def generate_earnest_money_rep(self):

        return self.env.ref('report_earnest_money.earnest_money_report_abc').report_action(self)


