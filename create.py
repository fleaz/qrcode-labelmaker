#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import os
import qrcode
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


@click.command()
@click.option('--template', '-t', help="Define the filename of the template to use")
@click.option('--owner', '-o', help="Write the owner onto the label")
@click.argument("name")
@click.argument("url")
def generator(template, owner, name, url):

    if not template:
        template = "default.html"

    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template(template)

    # generate qr-code
    qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3)

    qr.add_data(url)
    img = qr.make_image()
    img.save("qrcode.png")

    # Fill variables
    template_vars = {"name": name}
    if owner:
        template_vars["owner"] = owner

    # Render HTML template with variables
    html_out = template.render(template_vars)

    # Generate pdf
    HTML(string=html_out, base_url=os.path.realpath(__file__)).write_pdf("label.pdf")

if __name__ == "__main__":
    generator()

