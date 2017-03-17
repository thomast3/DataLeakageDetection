from django.db import models

# Create your models here.
class LoginDetails(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	designation = models.IntegerField(default=1)

	def __str__(self):
		return self.username