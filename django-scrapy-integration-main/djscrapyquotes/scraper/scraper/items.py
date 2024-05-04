# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import pathlib


class DiscoveredUrls(scrapy.Item):
    title = scrapy.Field()
    external_id = scrapy.Field()
    created_at = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
