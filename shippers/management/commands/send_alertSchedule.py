from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from vtracker.forms import *
from django.contrib import messages
from datetime import *
import calendar
from django.http import HttpResponse, JsonResponse
from dateutil.relativedelta import *
from tablib import *
from copy import deepcopy
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import os
import json
from django.contrib.auth.models import User
from django.db.models import Prefetch
import pdfkit


class Command(BaseCommand):
    def handle(self, *args, **options):
        path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        options = {
            "enable-local-file-access": None,
            "dpi": 365,
            "page-size": "A4",
            "margin-top": "0.25in",
            "margin-right": "0.25in",
            "margin-bottom": "0.25in",
            "margin-left": "0.25in",
            "encoding": "UTF-8",
            "custom-header": [("Accept-Encoding", "gzip")],
            "no-outline": None,
        }
        users = User.objects.all()
        production_lines = ProductionLine.objects.all()
        for user in users:
            production_lines_to_alert = []
            for production_line in production_lines:
                engineers = production_line.engineers.all()
                for engineer in engineers:
                    if user == engineer:
                        production_line_weeks = ProductionLineWeek.objects.filter(
                            production_line=production_line
                        ).values_list(flat=True)
                        for production_line_week in production_line_weeks:
                            production_line_week = ProductionLineWeek.objects.get(
                                pk=production_line_week
                            )
                            if (
                                (
                                    datetime.now().date()
                                    - production_line_week.start_date
                                ).days
                                >= production_line_week.day_start_alerts
                                and production_line_week.state == 0
                                and not production_line_week.no_production
                            ):
                                production_lines_to_alert.append(production_line_week)
            if len(production_lines_to_alert) > 0:
                msg_html = render_to_string(
                    "notifications/email/email.html",
                    {
                        "production_lines": production_lines_to_alert,
                        "production_linecount": len(production_lines_to_alert),
                    },
                )
                subject, from_email, to = (
                    "Daily Undelivered Control Plans",
                    "noreply@visteon.com",
                    "rui.nascimento@visteon.com",
                )
                text_content = "Good morning,<br><br>The daily alerts are ready for the deliveries which have yet to be delivered.<br>Check the attachments for a PDF containing all the information.<br><br>Best regards,<br>Visteon's VMETRO<br><br>(this email was automatic, do not reply to it)"
                html_content = msg_html
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.content_subtype = "html"
                pdf = pdfkit.from_string(
                    msg_html, False, configuration=config, options=options
                )
                msg.attach("alerts.pdf", pdf, "application/pdf")
                msg.send()
            else:
                continue
