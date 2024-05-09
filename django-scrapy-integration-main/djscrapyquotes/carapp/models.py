from django.db import models


class RunIDModel(models.Model):
    id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return self.id


class CarListingDiscovery(RunIDModel):
    parse_batch = models.CharField(max_length=50, blank=True, null=True)

    external_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(max_length=100, auto_now_add=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        unique_together = ('parse_batch', 'external_id')

