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


class CarListingDetails(models.Model):
    external_id = models.CharField(max_length=50)
    parse_batch = models.CharField(max_length=50, blank=True, null=True)
    manufactured_date = models.DateField(null=True, blank=True)
    engine = models.CharField(max_length=150, blank=True, null=True)
    power = models.CharField(max_length=150, blank=True, null=True)
    euro_standard = models.CharField(max_length=150, blank=True, null=True)
    gearbox = models.CharField(max_length=150, blank=True, null=True)
    odometer = models.CharField(max_length=150, blank=True, null=True)
    seller_name = models.CharField(max_length=150, blank=True, null=True)
    seller_phone = models.CharField(max_length=150, blank=True, null=True)
    seller_webpage = models.CharField(max_length=150, blank=True, null=True)
    full_location = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    posted = models.CharField(max_length=150, blank=True, null=True)
    adv_visits = models.CharField(max_length=150, blank=True, null=True)
    brand = models.CharField(max_length=150, blank=True, null=True)
    model = models.CharField(max_length=150, blank=True, null=True)
    price = models.CharField(max_length=150, blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    color = models.CharField(max_length=150, blank=True, null=True)
    engine_size = models.CharField(max_length=150, blank=True, null=True)
    posted_date = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        unique_together = ('parse_batch', 'external_id')
