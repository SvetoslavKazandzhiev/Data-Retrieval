# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from carapp.models import CarListingDiscovery

import logging, coloredlogs
logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)


class ScraperPipeline:


    def process_item(self, item, spider):
        try:
            CarListingDiscovery.objects.update_or_create(
                external_id=item['external_id'],
                title=item['title'],
                url=item['url'],
                price=item['price'],
            )
            print("\n")
            logger.warn("Loaded car listing {}".format(item['title']))
            print(item)
        except Exception as e:
            print("\n")
            logger.error("\nFailed to load car listing, Reason For Failure:{}".format(e))
            print(item)
        return item
