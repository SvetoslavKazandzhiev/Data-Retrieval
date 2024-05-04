from django.core.management import BaseCommand

import os
from pathlib import Path


class Command(BaseCommand):

    help = "Scrape the carapp"

    def handle(self, *args, **kwargs):
        django_path = Path(__file__).resolve().parent.parent.parent.parent

        os.chdir(str(django_path)+"/scraper")
        os.system("scrapy crawl discovery")
        
