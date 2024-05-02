from datetime import datetime

from django.db import models


class MobileListingDiscovery(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    date_published = models.DateTimeField(default=datetime.now())
    url = models.URLField(max_length=100, blank=True, null=True)