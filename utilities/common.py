from playwright.async_api import async_playwright
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utilities import constants as c

async def convert_html_to_pdf(html_filepath: str, output_filename: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 794, "height": 1123},  # A4
            device_scale_factor=3
        )

        await page.goto(f"file://{html_filepath}")  # ou une URL externe
        await page.pdf(
            path=f"{output_filename}",
            format="A4",
            print_background=True  # ✅ Active les background graphics,

        )
        await browser.close()


# Token settings

security = HTTPBearer()
def token_checking(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    print("token used", token)
    if token not in c.AUTHORIZED_TOKENS:
        raise HTTPException(status_code=401, detail="Invalid token")