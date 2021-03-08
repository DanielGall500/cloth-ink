from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=300)
	description = models.TextField()
	#TODO: image

	def __str__(self):
		return self.title