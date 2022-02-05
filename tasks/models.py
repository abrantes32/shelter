from turtle import mode
from django.db import models
from datetime import date

from shelter.settings import USE_TZ

class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS, ) # Se a tarefa está pronta ou não

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ShelterDATABASE(models.Model):
    hostname = models.TextField(null=True)
    ip_address = models.TextField(null=True, max_length=200)
    title = models.CharField(null=True, max_length=200)
    severity = models.TextField(null=True)
    cvss = models.TextField(null=True)
    publication_date = models.DateField(null=True)

    def __str__(self):
        return self.headline