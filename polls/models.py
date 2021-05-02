from django.db import models

class Telefon(models.Model):
    kompaniya_nomi = models.CharField(max_length=50)
    rusumi = models.CharField(max_length=50)
    xotirasi = models.IntegerField()
    tezkor_xotirasi = models.IntegerField()
    narxi = models.IntegerField()