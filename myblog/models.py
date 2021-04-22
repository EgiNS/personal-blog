from django.db import models

# Create your models here.

class Halaman(models.Model):
    gambar = models.ImageField(null=True, upload_to="static/image")
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=40)
    waktu = models.DateTimeField(auto_now_add=True)
    ringkasan = models.CharField(max_length=200, null=True)
    artikel = models.TextField()

    def __str__(self):
        return self.judul