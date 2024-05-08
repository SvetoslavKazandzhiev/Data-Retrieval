import scrapy
from scrapy_djangoitem import DjangoItem
import pathlib


class DiscoveredUrls(scrapy.Item):
    title = scrapy.Field()
    external_id = scrapy.Field()
    created_at = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    parse_batch = scrapy.Field()






