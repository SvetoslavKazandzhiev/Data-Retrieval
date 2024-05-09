import scrapy
from scrapy_djangoitem import DjangoItem
import pathlib
from carapp.models import CarListingDiscovery


class DiscoveredUrls(DjangoItem):
    django_model = CarListingDiscovery


