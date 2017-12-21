from __future__ import unicode_literals

from django.db import models

class IseService(models.Model):
	"""
		To save ise Service details
	"""
	ise_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	ise_data= models.TextField()