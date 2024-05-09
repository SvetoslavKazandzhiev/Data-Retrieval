from carapp.models import CarListingDiscovery, RunIDModel
import logging, coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)


class ScraperPipeline:

    def process_item(self, item, spider):
        if not CarListingDiscovery.objects.filter(external_id=item['external_id'],
                                                  parse_batch=item['parse_batch']).exists():
            try:
                CarListingDiscovery.objects.create(
                    external_id=item['external_id'],
                    title=item['title'],
                    url=item['url'],
                    price=item['price'],
                    description=item['description'],
                    parse_batch=item['parse_batch']
                )
                print("\n")
                logger.warn("Loaded car listing {}".format(item['title']))
                print(item)
            except Exception as e:
                print("\n")
                logger.error("\nFailed to load car listing, Reason For Failure:{}".format(e))
                print(item)
        return item

