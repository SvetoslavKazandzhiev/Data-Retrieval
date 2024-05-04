from django.db import models


class CarListingDiscovery(models.Model):
    external_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(max_length=100, auto_now_add=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.url
