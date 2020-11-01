from django.db import models
from django.utils import timezone
# Create your models here.

#客户：管理建筑工地工人信息
#派出所与工地联系渠道
#每个工地位置


class User(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(unique=True, max_length=32)

    password = models.CharField(max_length=64)

    registration_data = models.DateTimeField(default=timezone.now)

    token = models.CharField(max_length=32, unique=True,
                             null=True, editable=False)

    def __str__(self):
        return self.name


class ConstructionSite(models.Model):
    id = models.AutoField(primary_key=True, editable=False)

    name = models.CharField(max_length=32)

    address = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ConstructionSitePersonnel(models.Model):
    construction_site_id = models.IntegerField()

    worker_id = models.IntegerField()


class Worker(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, default=1)

    name = models.CharField(max_length=32)

    sex = models.CharField(max_length=1)

    nation = models.CharField(max_length=8)

    id_number = models.CharField(max_length=20)

    residential_address = models.CharField(max_length=20)

    registration_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
