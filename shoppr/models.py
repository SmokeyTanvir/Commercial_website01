from django.db import models

# Create your models here.
class Item(models.Model):
	item_img = models.ImageField(upload_to='items', default="")
	item_name = models.CharField(max_length=64)
	item_desc = models.CharField(max_length=64)

	def __str__(this):
		return this.item_name