from odoo import models,api,fields
from datetime import datetime
from datetime import timedelta
import math



class DetailXlsxTemplate(models.AbstractModel):
    _name = 'report.report_tender_status.detailed_xlsx_template'
    _description = "Tender Status Report"
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, report_detail, wizard_data):

        merge_format = workbook.add_format({
            'bold': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': '17',
            "font_color": 'black',
            'font_name': 'Metropolis',
        })

        merge_format_date = workbook.add_format({
            'bold': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': '15',
            "font_color": 'black',
            'font_name': 'Metropolis',
            'num_format': 'd mmm yyyy'
        })

        format_form = workbook.add_format({
            "bold": 1,
            "border": 1,
            "align": 'center',
            "valign": 'vcenter',
            "font_color": 'black',
            "bg_color": '#ffe3cc',
            'font_size': '10',
            'font_name': 'Metropolis',
            'num_format': '#,##0',
        })

        format_form_1 = workbook.add_format({
            "bold": 1,
            "border": 1,
            "align": 'center',
            "valign": 'vcenter',
            "font_color": 'blue',
            "bg_color": '#ffe3cc',
            'font_size': '10',
            'font_name': 'Metropolis',
            'num_format': '#,##0',
        })

        format_form_2 = workbook.add_format({
            "bold": 1,
            "border": 1,
            "align": 'center',
            "valign": 'vcenter',
            "font_color": 'black',
            "bg_color": 'yellow',
            'font_size': '10',
            'font_name': 'Metropolis',
            'num_format': '#,##0',
        })

        format_form_3 = workbook.add_format({
            "bold": 1,
            "border": 1,
            "align": 'center',
            "valign": 'vcenter',
            "font_color": 'blue',
            "bg_color": 'yellow',
            'font_size': '10',
            'font_name': 'Metropolis',
            'num_format': '#,##0',
        })

        worksheet = workbook.add_worksheet('Report')
        # head = ' Report'
        # worksheet.set_row(3, 30)
        # worksheet.set_row(4, 30)
        # worksheet.merge_range('A1:Q2', head, merge_format)
        worksheet.set_column('A:AZ', 20)

        rows = 0



        # new_time= datetime.now()+timedelta(hours=5)
        worksheet.write_string(rows, 0, 'S.No', format_form)
        worksheet.write_string(rows, 1, 'Customer Name', format_form)
        worksheet.write_string(rows, 2, 'Quotation No.', format_form)
        worksheet.write_string(rows, 3, 'Tender No', format_form)
        worksheet.write_string(rows, 4, 'Month', format_form)
        worksheet.write_string(rows, 5, 'Purchasing Date', format_form)
        worksheet.write_string(rows, 6, 'Date Of Submission', format_form)
        worksheet.write_string(rows, 7, 'Date Of Opening', format_form)
        worksheet.write_string(rows, 8, 'Total Value', format_form)
        worksheet.write_string(rows, 9, 'Earnest Money', format_form)
        worksheet.write_string(rows, 10, 'Status', format_form)
        worksheet.write_string(rows, 11, 'Confirmation Date', format_form)
        worksheet.write_string(rows, 12, 'Remarks', format_form)
        worksheet.write_string(rows, 13, 'Quotations', format_form)
        worksheet.write_string(rows, 14, 'Competitor Analysis Report', format_form)
        worksheet.write_string(rows, 15, 'Earnest Money No.', format_form)
        worksheet.write_string(rows, 16, 'Amount', format_form)
        worksheet.write_string(rows, 17, 'Total Received', format_form)
        worksheet.write_string(rows, 18, 'Pending', format_form)
        worksheet.write_string(rows, 19, 'Due On', format_form)
        worksheet.write_string(rows, 20, 'OverDue', format_form)
        worksheet.write_string(rows, 21, 'Security Money No.', format_form)
        worksheet.write_string(rows, 22, 'Amount', format_form)
        worksheet.write_string(rows, 23, 'Total Received', format_form)
        worksheet.write_string(rows, 24, 'Pending', format_form)
        worksheet.write_string(rows, 25, 'Due On', format_form)
        worksheet.write_string(rows, 26, 'OverDue', format_form)

