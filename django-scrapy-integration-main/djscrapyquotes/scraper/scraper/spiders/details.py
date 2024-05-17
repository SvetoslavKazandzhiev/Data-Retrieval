import re
import scrapy
from ..items import DetailsMobileBG
from .read_data import GetLastBatch
from pyquery import PyQuery as pq

get_data = GetLastBatch()
urls = get_data.get_last_batch_urls()


class DetailsMobileSpider(scrapy.Spider):
    """Extracts the car details on daily basis"""

    custom_settings = {
        'CONCURRENT_REQUESTS': 5,
        'DOWNLOAD_DELAY': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'CONCURRENT_REQUESTS_PER_IP': 4,
        'FEED_EXPORT_ENCODING': 'windows-1251',
    }
    # parse_batch = get_data.get_last_batch_number()
    name = "details"
    start_urls = [item[0] for item in urls]
    # print(parse_batch)
    def parse(self, response, **kwargs):
        item = DetailsMobileBG()
        source = response.body
        d = pq(source)
        print(source)
        parse_batch = '350'
        url = response.url
        print(url)
        pattern = r'\d{17}'
        match = re.search(pattern, url)
        external_id = match.group(0)
        manufactured_date = d('div.mainCarParams .proizvodstvo .mpInfo').text()
        engine = d('div.mainCarParams .dvigatel .mpInfo').text()
        power = d('div.mainCarParams .moshtnost .mpInfo').text().replace('к.с.', '').strip()
        euro_standard = d('div.mainCarParams .euro .mpInfo').text().strip()
        gearbox = d('div.mainCarParams .skorosti .mpInfo').text()
        odometer = d('div.mainCarParams .probeg .mpInfo').text().replace('км', '').strip()
        seller_name = d('div.infoBox .name').text()
        seller_phone = d('div.infoBox .phone').text()
        seller_webpage = d('div.infoBox .text a').attr('href')
        seller_address1 = d('div.infoBox .region').text().replace('Регион:', '').strip()
        seller_address2 = d('div.infoBox .adress').text().replace('Местоположение:', '').strip()
        full_location = seller_address1 + seller_address2
        city = d('.carLocation').text().replace('Намира се в', '').replace('гр.', '').strip()
        adv_visits = d(' div.left > div.statistiki > div.text > strong').text()
        brand = self.get_value_from_regex(r"AdvertBrand', \['([^']+)'\]", source)
        model = self.get_value_from_regex(r"AdvertModel', \['([^']+)'\]", source)
        price = self.get_value_from_regex(r"AdvertPrice', \['([^']+)'\]", source)
        category = self.get_value_from_regex(r"AdvertCategory', \['([^']+)'\]", source)
        color = self.get_value_from_regex(r'<div>\s*Цвят\s*</div>\s*<div>\s*(.*?)\s*</div>', source)
        engine_size = self.get_value_from_regex(r'<div>\s*Кубатура \[куб\.см\]\s*</div>\s*<div>\s*(.*?)\s*</div>', source)
        posted = d('.statistiki .text').text()

        try:
            pattern = r'(\d{1,2}\s[а-я]+\s\d{4}\sг\.)'
            posted_date = re.findall(pattern, posted)
            item['posted_date'] = posted_date[0].replace('г.', '').strip()
        except:
            item['posted_date'] = None
            posted_date = item['posted_date']

        item['external_id'] = external_id
        item['manufactured_date'] = manufactured_date
        item['parse_batch'] = parse_batch
        item['engine'] = engine
        item['power'] = power
        item['euro_standard'] = euro_standard
        item['gearbox'] = gearbox
        item['odometer'] = odometer
        item['seller_name'] = seller_name
        item['seller_phone'] = seller_phone
        item['seller_webpage'] = seller_webpage
        item['full_location'] = full_location
        item['city'] = city
        item['posted'] = posted_date
        item['adv_visits'] = adv_visits
        item['brand'] = brand
        item['model'] = model
        item['price'] = price
        item['category'] = category
        item['color'] = color
        item['engine_size'] = engine_size

        yield item

    @staticmethod
    def get_value_from_regex(rgx, source):
        try:
            value = re.search(rgx, source.group(1))
        except:
            value = None
        return value




