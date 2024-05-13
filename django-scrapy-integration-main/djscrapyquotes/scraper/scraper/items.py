import scrapy
from scrapy_djangoitem import DjangoItem
import pathlib
from carapp.models import CarListingDiscovery, CarListingDetails


class DiscoveredUrls(DjangoItem):
    django_model = CarListingDiscovery


class DetailsMobileBG(DjangoItem):
    django_model = CarListingDetails

