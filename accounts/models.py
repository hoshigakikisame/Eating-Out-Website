from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restorant(models.Model):
	milik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restorant')
	STATUS1 = (
			('Buka', 'Buka'),
			('Tutup', 'Tutup'),


		)
	foto_resto = models.ImageField(upload_to="documents/", default="/default.jpg")
	foto_menu = models.ImageField(upload_to="documents/", default="/default.jpg")
	nama_resto = models.CharField(max_length = 50, null = True)
	notlp = models.CharField(max_length = 12, null = True)
	alamat = models.CharField(max_length = 50, null = True)
	status = models.CharField(max_length = 50, null = True , choices = STATUS1)
	deskripsi = models.TextField(null = True)

	def save(self,  *args, **kwargs ):
		super(Restorant, self).save(*args, **kwargs)
		super().save()


	def __str__(self):
		return self.nama_resto

class Menu(models.Model):
	penyedia = models.ForeignKey(Restorant, on_delete=models.CASCADE)
	status = models.BooleanField()
	STATUS2 = (
			('Tersedia', 'Tersedia'),
			('Habis', 'Habis'),
		)

	nama_menu = models.CharField(max_length = 50, null = True)
	harga = models.IntegerField(null = True)
	deskripsi = models.TextField(null = True)
	status = models.CharField(max_length = 50, null = True, choices = STATUS2)

	def __str__(self):
		return self.nama_menu