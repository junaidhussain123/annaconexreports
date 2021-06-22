from odoo import models, api, fields

from datetime import datetime



class DetailWizard(models.TransientModel):
    _name = "security.deposit.wizard"
    _description = "Security Deposit  Wizard"
    # _inherit = 'pos.config'

    customer_name = fields.Many2one('res.partner',string="By Customer Name",)
    by_date_of_making = fields.Char(string='By Date Of Making')
    by_tender_no = fields.Char(string='By Tender No in case of Earnest Money')

    by_loi_no = fields.Char(string='By LOI No in case of Earnest Money')
    by_instrument_no = fields.Char(string='By Instrument No')
    by_favour = fields.Char(string='By Favour Of')
    by_cheque_no = fields.Char(string='By Cheque No')
    by_bank = fields.Char(string='By Bank')
    by_voucher_type = fields.Char(string='By Voucher Type')
    by_amount = fields.Char(string='By Amount')
    by_pending_amount = fields.Char(string='By Pending Amount')
    By_closing_date = fields.Datetime(string='By Closing Date & Time')

    def security_deposit_report(self):

        return self.env.ref('report_security_deposit.security_deposit_report').report_action(self)


