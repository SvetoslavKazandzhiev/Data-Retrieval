from itemadapter import ItemAdapter
import uuid
from carapp.models import CarListingDiscovery, RunIDModel
from django.shortcuts import get_object_or_404

import logging, coloredlogs
logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)


class ScraperPipeline:

    # def __init__(self):
    #     self.run_id = str(uuid.uuid4())

    def process_item(self, item, spider):
        # try:
        #     batch_instance = RunIDModel.objects.get(pk=self.run_id)  # Create a batch instance
        #     car_listing_instance = CarListingDiscovery(parse_batch=batch_instance)  # Assign the batch instance to the car_listing_instance
        #     car_listing_instance.save()
        # except Exception as e:
        #     print("\n")
        #     logger.error("\nFailed to create batch number, Reason For Failure:{}".format(e))



        try:
            CarListingDiscovery.objects.create(
                external_id=item['external_id'],
                title=item['title'],
                url=item['url'],
                price=item['price'],
                parse_batch_id=item['parse_batch']
            )
            print("\n")
            logger.warn("Loaded car listing {}".format(item['title']))
            print(item)
        except Exception as e:
            print("\n")
            logger.error("\nFailed to load car listing, Reason For Failure:{}".format(e))
            print(item)
        return item
