import scrapy
# from ..items import CarListingDiscovery
from .read_data import data_reader

class DetailsMobileSpider(scrapy.Spider):
    """Extracts the car details on daily basis"""

    FEED_EXPORT_ENCODING = 'windows-1251'
    name = "details"
    start_urls = [item[0] for item in data_reader()]

    def parse(self, response, **kwargs):
        print(response.body)
        # item = CarListingDiscovery()
        #
        # all_div_quotes = response.css('div.quote')
        # for quote in all_div_quotes:
        #     title = quote.css('span.text::text').extract_first().replace('”', '').replace("“", "")
        #     author = quote.css('.author::text').extract_first()
        #
        #     # Check if author's name matches
        #     if author.strip().lower() == self.author.strip().lower():
        #         item['text'] = title
        #         item['author'] = author
        #         yield item
        #
        # # Crawl Next Page
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)