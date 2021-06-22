from odoo import models,api,fields
from datetime import datetime
from datetime import timedelta
import math



class DetailXlsxTemplate(models.AbstractModel):
    _name = 'report.report_competitor_analysis.detailed_xlsx_template'
    _description = "Competitor Analysis Report"
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
        worksheet.write_string(rows, 0, 'Customer Name', format_form)
        rows+=1
        worksheet.write_string(rows, 0, 'Tender No.', format_form)
        rows += 1
        worksheet.write_string(rows, 0, 'Date', format_form)
        rows += 1
        worksheet.write_string(rows, 0, 'Value', format_form)
        rows += 2
        worksheet.write_string(rows, 0, 'Quotation No.', format_form)
        rows += 2
        worksheet.write_string(rows, 0, 'Competitor Report NO.', format_form)
        rows += 2
        worksheet.write_string(rows, 3, 'Competitor 1', format_form)
        worksheet.write_string(rows, 4, 'Competitor 2', format_form)
        worksheet.write_string(rows, 5, 'Competitor 3', format_form)
        worksheet.write_string(rows, 6, 'Competitor 4', format_form)
        worksheet.write_string(rows, 7, 'Competitor 5', format_form)
        worksheet.write_string(rows, 8, 'Win By Lowest', format_form)
        rows+=1




        # new_time= datetime.now()+timedelta(hours=5)
        worksheet.write_string(rows, 0, 'Sr.', format_form)
        worksheet.write_string(rows, 1, 'Items', format_form)
        worksheet.write_string(rows, 2, 'Riz Tech', format_form)
        worksheet.write_string(rows, 3, 'Jamal & Brothers', format_form)
        worksheet.write_string(rows, 4, 'Pak Land', format_form)
        worksheet.write_string(rows, 5, 'Smart Net', format_form)
        worksheet.write_string(rows, 6, 'AK Enterprises', format_form)
        worksheet.write_string(rows, 7, 'Zain Tech', format_form)


