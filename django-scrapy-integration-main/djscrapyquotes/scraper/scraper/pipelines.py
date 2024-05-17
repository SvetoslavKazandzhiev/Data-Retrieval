from carapp.models import CarListingDiscovery, RunIDModel, CarListingDetails
import logging, coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)


class ScraperPipeline:

    def process_item(self, item, spider):
        if not CarListingDiscovery.objects.filter(
                external_id=item['external_id'],
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


class ScraperDetailsPipeline:
    def process_item(self, item, spider):
        if not CarListingDetails.objects.filter(
                external_id=item['external_id'],
                parse_batch=item['parse_batch']).exists():
            try:
                CarListingDetails.objects.create(
                    external_id=item['external_id'],
                    parse_batch=item['parse_batch'],
                    manufactured_date=item['manufactured_date'],
                    engine=item['engine'],
                    power=item['power'],
                    euro_standard=item['euro_standard'],
                    gearbox=item['gearbox'],
                    odometer=item['odometer'],
                    seller_name=item['seller_name'],
                    seller_phone=item['seller_phone'],
                    seller_webpage=item['seller_webpage'],
                    full_location=item['full_location'],
                    city=item['city'],
                    posted=item['posted'],
                    adv_visits=item['adv_visits'],
                    brand=item['brand'],
                    model=item['model'],
                    price=item['price'],
                    category=item['category'],
                    color=item['color'],
                    engine_size=item['engine_size'],
                )
                print("\n")
                logger.warn("Loaded car {}".format(item['title']))
                print(item)
            except Exception as e:
                print("\n")
                logger.error("\nFailed to load car, Reason For Failure:{}".format(e))
                print(item)

        return item
