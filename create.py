#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime
import qrcode

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")

# generate qr-code
qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3
    )
qr.add_data('https://wiki.darmstadt.ccc.de/Projekte/3D-Drucker')
img = qr.make_image()
img.save("qrcode.png")

# Fill variables
template_vars = {"title": "3D-Drucker", "owner": "fleaz"}

# Render template
html_out = template.render(template_vars)

# Generate pdf
HTML(string=html_out, base_url="/home/fleaz/workspace/python/qrcode-labels").write_pdf("label.pdf")

