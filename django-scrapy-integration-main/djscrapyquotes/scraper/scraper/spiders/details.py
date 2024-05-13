import re
import scrapy
from ..items import DetailsMobileBG
from .read_data import GetLastBatch
from pyquery import PyQuery as pq

get_data = GetLastBatch()
urls = get_data.get_last_batch_urls()


class DetailsMobileSpider(scrapy.Spider):
    """Extracts the car details on daily basis"""

    FEED_EXPORT_ENCODING = 'windows-1251'
    name = "details"
    start_urls = [item[0] for item in urls]

    def parse(self, response, **kwargs):
        item = DetailsMobileBG()
        d = pq(response.body)

        item['creation_date'] = d('div.mainCarParams .proizvodstvo .mpInfo').text()
        item['engine'] = d('div.mainCarParams .dvigatel .mpInfo').text()
        item['power'] = d('div.mainCarParams .moshtnost .mpInfo').text().replace('к.с.', '').strip()
        item['euro_standard'] = d('div.mainCarParams .euro .mpInfo')
        item['gearbox'] = d('div.mainCarParams .skorosti .mpInfo').text()
        item['odometer'] = d('div.mainCarParams .probeg .mpInfo').text().replace('км', '').strip()
        item['seller_name'] = d('div.infoBox .name').text()
        item['seller_phone'] = d('div.infoBox .phone').text()
        item['seller_webpage'] = d('div.infoBox .text a').attr('href')
        seller_address1 = d('div.infoBox .region').text().replace('Регион:', '').strip()
        seller_address2 = d('div.infoBox .adress').text().replace('Местоположение:', '').strip()
        item['full_location'] = seller_address1 + seller_address2
        item['city'] = d('.carLocation').text().replace('Намира се в', '').replace('гр.', '').strip()
        item['posted'] = d('.statistiki .text').text()
        item['adv_visits'] = d(' div.left > div.statistiki > div.text > strong').text()
        item['brand'] = self.get_value_from_regex(r"AdvertBrand', \['([^']+)'\]", d.html())
        item['model'] = self.get_value_from_regex(r"AdvertModel', \['([^']+)'\]", d.html())
        item['price'] = self.get_value_from_regex(r"AdvertPrice', \['([^']+)'\]", d.html())
        item['category'] = self.get_value_from_regex(r"AdvertCategory', \['([^']+)'\]", d.html())
        item['color'] = self.get_value_from_regex(r'<div>\s*Цвят\s*</div>\s*<div>\s*(.*?)\s*</div>', d.html())
        item['engine_size'] = self.get_value_from_regex(r'<div>\s*Кубатура \[куб\.см\]\s*</div>\s*<div>\s*(.*?)\s*</div>', d.html())

        try:
            pattern = r'(\d{1,2}\s[а-я]+\s\d{4}\sг\.)'
            posted_date = re.findall(pattern, d('.statistiki .text').text())
            item['posted_date'] = posted_date[0].replace('г.', '').strip()
        except:
            item['posted_date'] = None

        yield item

    @staticmethod
    def get_value_from_regex(rgx, source):
        try:
            value = re.search(rgx, source.group(1))
        except:
            value = None
        return value




        # # Crawl Next Page
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)