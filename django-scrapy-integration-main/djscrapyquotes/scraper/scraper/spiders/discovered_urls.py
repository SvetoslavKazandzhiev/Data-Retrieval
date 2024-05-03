import scrapy
from ..items import DiscoveredUrls


class QuotesSpider(scrapy.Spider):

    start_urls = ['https://www.mobile.bg/obiavi/avtomobili-dzhipove/bmw']
    name = "discovery"
    FEED_EXPORT_ENCODING = 'windows-1251'

    def parse(self, response, **kwargs):
        item = DiscoveredUrls()
        print(response.body)
        # LISTING URLS
        # data = set([item('a').attr('href') for item in response.css('form table.tablereset').get()])
        # data = [item.replace('//', 'https://') for item in data if item.startswith('//')]
        # for dat in data:
        #     print(dat)

        # urls = response.css('form table.tablereset')
        # for url in urls:
        #     title = quote.css('span.text::text').extract_first().replace('”', '').replace("“", "")
        #     author = quote.css('.author::text').extract_first()
        #
        #     item['external_id'] = external_id
        #     item['created_at'] = created_at
        #     item['url'] = url
        #     item['price'] = price
        #     yield item
        #
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)