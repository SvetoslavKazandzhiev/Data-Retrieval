from django.db import models


class CarListingDiscovery(models.Model):
    external_id = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.TextField()
    price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.url
