from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse

from services import InvoiceService
from utilities.common import token_checking

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/download-invoice/{invoice_id}")
async def download_invoice_pdf(invoice_id: str, token: str = Depends(token_checking)):

    print("token (used) : ", token)

    output_pdf_file,  output_pdf_filename =  await InvoiceService.InvoiceService.retrieve_pdf_invoice(invoice_id)

    # returns pdf file
    return FileResponse(
        path=output_pdf_file,
        media_type='application/pdf',
        filename=output_pdf_filename
    )
