from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)


class Image(models.Model):
    image = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)


class CsvFile(models.Model):
    url = models.CharField(max_length=300)
    uploaded = models.DateTimeField(auto_now=True)
    activate = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
