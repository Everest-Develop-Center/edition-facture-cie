from playwright.sync_api import sync_playwright
import os
from PIL import Image


chemin_fichier = os.path.abspath("templates/normal/index.html")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 794, "height": 1123},
        device_scale_factor=3
    )
    page.goto(f"file://{chemin_fichier}")  # ou une URL externe
    page.pdf(
        path="mon_fichier.pdf",
        format="A4",
        print_background=True # ✅ Active les background graphics,

    )
    #page.screenshot(path="sortie3.jpg", full_page=False)

    browser.close()