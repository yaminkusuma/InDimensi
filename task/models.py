from django.db import models

# Create your models here.

# class login (models.Model):
#     email = models.CharField(max_length=30)
#     password = models.CharField(max_length=8)

class buatproject(models.Model):
    nama = models.CharField(max_length=50)
    judul = models.CharField(max_length=50)
    type_user = models.CharField(max_length=50)
    jenis_jasa = models.CharField(max_length=50)
    alamat_jasa = models.CharField(max_length=50)
    price_jasa = models.IntegerField()
    deadline_jasa = models.CharField(max_length=50)
    catatan = models.TextField(max_length=1000)
