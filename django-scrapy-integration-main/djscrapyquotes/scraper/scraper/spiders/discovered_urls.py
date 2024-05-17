import re
import datetime
import scrapy
from ..items import DiscoveredUrls
from carapp.models import RunIDModel, CarListingDiscovery
from .utilitys import text

import codecs
from pyquery import PyQuery as pq
from datetime import datetime


class DiscoveryMobileBGSpider(scrapy.Spider):

    start_urls = ['https://www.mobile.bg/obiavi/avtomobili-dzhipove/bmw']
    name = "discovery"
    FEED_EXPORT_ENCODING = 'windows-1251'

    def parse(self, response, **kwargs):
        item = DiscoveredUrls()
        run_id_instance = RunIDModel.objects.create()
        parse_batch = run_id_instance.id

        # LISTING DATA
        d = pq(response.body)
        data_container = d('div .TOP')

        for data in data_container.items():
            title = data(' div.text > div.zaglavie > a').text()
            url = data(' div > div.big > a').attr('href').replace('//', 'https://')
            description = text.clean_emoji(data('.info').text())
            price = data('.DOWN').text() or data('.price').text()
            price = price.replace('лв.', '').strip()
            pattern = r'\d{17}'
            match = re.search(pattern, url)
            external_id = match.group(0)

            item['title'] = title
            item['external_id'] = external_id
            item['created_at'] = datetime.now()
            item['url'] = url
            item['price'] = price
            item['description'] = description
            item['parse_batch'] = parse_batch
            yield item

        # # Crawl Next Page
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)