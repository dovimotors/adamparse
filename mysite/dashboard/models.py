from django.db import models

# Create your models here.


class PartsInv(models.Model):

    #def __str__(self):
    #   return self.statdate

    statdate = models.DateField(auto_now=True)
    invvalue = models.FloatField()

class ServiceRO(models.Model):

    statdate = models.DateField(auto_now=True)
    totalrocount = models.IntegerField()
    oldrocount = models.IntegerField()
    printedrocount = models.IntegerField()
    printedro_custpay = models.FloatField()
    printedro_intpay = models.FloatField()
    printedro_warpay = models.FloatField()
    printedro_extpay = models.FloatField()
