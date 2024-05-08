from django.db import models
from django.urls import reverse
import uuid


class RunIDModel(models.Model):
    run_id = models.AutoField(primary_key=True)


class CarListingDiscovery(models.Model):
    parse_batch = models.ForeignKey(RunIDModel, on_delete=models.CASCADE)

    external_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(max_length=100, auto_now_add=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        unique_together = ('parse_batch', 'external_id')

