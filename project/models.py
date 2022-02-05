from turtle import mode
from django.db import models

from shelter.settings import USE_TZ

class Vulnerability(models.Model):
    hostname = models.TextField(null=True)
    ip_address = models.TextField(null=True, max_length=200)
    title = models.CharField(null=True, max_length=200)
    severity = models.TextField(null=True)
    cvss = models.TextField(null=True)
    publication_date = models.DateField(null=True)

    def __str__(self):
        return self.headline