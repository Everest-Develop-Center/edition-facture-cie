import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMP_DIR = BASE_DIR / "temp"
NORMAL_INVOICE_TEMPLATE = BASE_DIR / "templates" / "normal" / "index.html"
NORMAL_INVOICE_TEMPLATE_DIR = BASE_DIR / "templates" / "normal"


# TOKEN PARAMS
AUTHORIZED_TOKENS = [
    "bWKoGqmjDBy9UPmJ2dtD7a97X4i6lbYrFecsE2GCMuLFMKLiGABbIO8KEiQ1Gey6", # mobile
    "p4ECBssYDCMppFpqzCJMX9o4T6VRe2XZJoAuBZI3XQs7SGQRvXubad5pf7wLDBqG", # web
    "0F2Rb0kEzRy6xgzCBBSZ4PmsWPjXgbSAIp9qSVUSkvhUEWLyE5lK790WzKokJum1", # mobile (clem bot)
    "UOfg8LbLmRDYFXe0lkJeTv8scyIZGmlAXsJMzBo5KHlrvLRMAxcke30pM96JldIx"  # web (clem bot)
]