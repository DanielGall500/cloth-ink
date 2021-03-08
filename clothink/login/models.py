from django.db import models

# Create your models here.
class Login(models.Model):
	name = models.CharField(max_length=300)
	password = models.TextField()

	def __str__(self):
		return self.name

class Registration(models.Model):
	name = models.CharField(max_length=300)
	password = models.TextField()

	def __str__(self):
		return self.name