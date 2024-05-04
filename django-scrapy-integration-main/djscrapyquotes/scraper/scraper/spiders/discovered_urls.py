import re
import datetime
import scrapy
from ..items import DiscoveredUrls
import codecs
from pyquery import PyQuery as pq
from datetime import datetime


class QuotesSpider(scrapy.Spider):

    start_urls = ['https://www.mobile.bg/obiavi/avtomobili-dzhipove/bmw']
    name = "discovery"
    FEED_EXPORT_ENCODING = 'windows-1251'

    def parse(self, response, **kwargs):
        item = DiscoveredUrls()

        d = pq(response.body)
        data_container = d('form table.tablereset td td')
        for data in data_container.items():
            title = data('img').attr('alt').replace('Обява за продажба на', '').split('~')[0].strip()
            price = data('img').attr('alt').replace('Обява за продажба на', '').replace('лв.', '').split('~')[-1].strip()
            url = data('a').attr('href')
            pattern = r'\d{17}'
            match = re.search(pattern, url)
            external_id = match.group(0)

            item['title'] = title
            item['external_id'] = external_id
            item['created_at'] = datetime.now()
            item['url'] = url
            item['price'] = price
            yield item

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