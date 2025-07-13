from models.invoiceDTO import InvoiceDTO

from utilities import constants as c, common, helper as h
from jinja2 import Template
from time import time
import random as ran

class InvoiceService:

    @staticmethod
    def retrieve_bill_from_external_source(invoice_id: str):
        return InvoiceDTO(id=str(ran.randint(1, 400)), period="04/2025", payment_deadline="30/06/2025",
                            bill_amount="{:,}".format(ran.randint(1000, 100000)).replace(",", " "),
                            customer_info=None, regional_direction="", credit_notes="", outstanding_amount="",
                            consumption_details=None, message_to_the_customer="")

    @staticmethod
    async def retrieve_pdf_invoice(invoice_id: str):
        # retrieve invoice raw data
        invoice = InvoiceService.retrieve_bill_from_external_source(invoice_id)

        # read invoice template
        with open(str(c.NORMAL_INVOICE_TEMPLATE), "r", encoding="utf-8") as f:
            template = Template(f.read())
        html_modified = template.render(bill_id=invoice.id, bill_amount=invoice.bill_amount,
                                        deadline_payment=invoice.payment_deadline, dr="Abidjan Nord")

        # generate temporary invoice in html format
        timestamp = int(time())
        html_filename_abs_path = c.NORMAL_INVOICE_TEMPLATE_DIR / f"invoice_{id}_{timestamp}.html"
        with open(str(html_filename_abs_path), "w") as f:
            f.write(html_modified)

        # convert html invoice into pdf
        output_pdf_filename = f"invoice_{id}_{timestamp}.pdf"
        output_pdf_file = str(c.TEMP_DIR / f"{output_pdf_filename}")
        await common.convert_html_to_pdf(html_filename_abs_path, output_pdf_file)

        # delete html temporary invoice file
        h.delete_file(html_filename_abs_path)

        return output_pdf_file, output_pdf_filename



