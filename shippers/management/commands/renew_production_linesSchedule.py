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

# Função Principal para envio dos emails
# Utilizar o task scheduler do windows, e nas acçoes colocar:
# Program/script: cmd         Add arguments (optional): /c batch_vreport_clopes4.bat         Start in(optional): C:\visteon\vreport\management\commands


class Command(BaseCommand):
    def handle(self, *args, **options):
        production_lines = ProductionLineWeek.objects.filter(active=True)
        production_lines = production_lines.order_by("-end_date")
        unique_production_lines = []
        for ordered_production_line in production_lines:
            exists_in_unique_production_lines = False
            for unique_production_line in unique_production_lines:
                if (
                    ordered_production_line.name == unique_production_line.name
                    and ordered_production_line.unique_code
                    == unique_production_line.unique_code
                ):
                    exists_in_unique_production_lines = True
            if not exists_in_unique_production_lines:
                unique_production_lines.append(ordered_production_line)
        for processed_production_line in unique_production_lines:
            if (
                processed_production_line.end_date < datetime.now().date()
                and processed_production_line.active is True
            ):
                clone_production_line = deepcopy(processed_production_line)
                clone_production_line.pk = None
                clone_production_line.delivered_by = None
                clone_production_line.state = False
                next_week = clone_production_line.start_date
                next_week = next_week + timedelta(days=-next_week.weekday(), weeks=1)
                clone_production_line.start_date = next_week
                while next_week.weekday() != 4:
                    next_week += timedelta(1)
                clone_production_line.end_date = next_week
                clone_production_line.save()
            else:
                continue
