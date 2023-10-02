from django.db import models

# Create your models here.

class Tower(models.Model):
    uuid = models.CharField(max_length=50)
    level = models.IntegerField(default=0)
    pump = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Башня'
        verbose_name_plural = 'Башня'

class TowerActivity(models.Model):
    tower = models.ForeignKey(Tower, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Історія'
        verbose_name_plural = 'Історія'
