from django.db import models


class CryptoPrice(models.Model):
    name = models.CharField(max_length=225)
    symbol = models.CharField(max_length=10)
    price = models.FloatField()
    last_update = models.DateTimeField(auto_now=True)