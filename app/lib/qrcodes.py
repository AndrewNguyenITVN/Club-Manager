"""
Manage library for creating QR Codes.

Reference: https://realpython.com/python-generate-qr-code/
"""

import uuid
import segno

from django.utils import timezone

from utils.files import get_media_dir


def create_qrcode_image(url: str):
    """Create QR Code image, return file path."""

    img_path = get_media_dir(f"{uuid.uuid4()}-{timezone.now().isoformat()}.png")

    qrcode = segno.make_qr(url)
    qrcode.save(img_path)

    return img_path