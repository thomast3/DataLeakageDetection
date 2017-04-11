from django.db import models

# Create your models here.
class Document(models.Model):
	title = models.CharField(max_length=50,default='null')
	description = models.CharField(max_length=500, blank=True)
	accesslevel = models.CharField(max_length=50, default=4)
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title