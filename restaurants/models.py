from django.db import models


class Restaurants(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    location = models.CharField(max_length=10, blank=False, null=False)
    xco = models.FloatField(max_length=20)
    yco = models.FloatField(max_length=20)
    upinfo = models.CharField(max_length=500)  # 즉 250자 까지 허용, 250자 맞는지 확인 필요
    downinfo = models.CharField(max_length=500)
    resnumber = models.CharField(max_length=16)
    mainpic = models.CharField(max_length=500)
    menupic = models.CharField(max_length=500)
    respic = models.CharField(max_length=500)
    category = models.CharField(max_length=5, default='밥집')
