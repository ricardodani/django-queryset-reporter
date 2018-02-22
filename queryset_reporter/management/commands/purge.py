#-*- encoding=utf-8 -*-
import os
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Purge xlsx and csvs'

    def handle(self, *args, **options):
        directories = ['xlsx', 'csvs']
        for directory in directories:
            path = os.path.join(settings.MEDIA_ROOT, directory)
            files = os.listdir(path)
            purge_date = datetime.now() - timedelta(days=7)
            for file in files:
                file = os.path.join(path, file)
                file_date = datetime.fromtimestamp(os.path.getmtime(file))
                print file_date
                if file_date < purge_date:
                    os.remove(file)
