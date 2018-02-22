#-*- encoding=utf-8 -*-
from datetime import datetime

from django.core.management.base import BaseCommand

from queryset_reporter.models import Queryset
from queryset_reporter.core import Reporter


class Command(BaseCommand):
    help = 'Automatic report generation'

    def handle(self, *args, **options):
        querysets = Queryset.objects.filter(automatic_generation=True)
        for queryset in querysets:
            reporter = Reporter(queryset, None)
            xlsx = reporter.render_xlsx()
            queryset.last_automatic_generation_at = datetime.now()
            queryset.last_automatic_generation_xlsx = xlsx
            queryset.save()
