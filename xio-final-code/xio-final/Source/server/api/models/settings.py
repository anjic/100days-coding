from __future__ import unicode_literals

from django.db import models
from api.models.ise_models import ListIse


class MailUser(models.Model):
	"""
	To store san details
	"""
	ise_id = models.ForeignKey(ListIse,on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	email = models.EmailField(blank=True)
	critical = models.BooleanField(blank=True,default=False)
	severe = models.BooleanField(blank=True,default=False)
	error = models.BooleanField(blank=True,default=False)
	normal = models.BooleanField(blank=True,default=False)
	warning = models.BooleanField(blank=True,default=False)
	informational = models.BooleanField(blank=True,default=False)
	is_active = models.BooleanField(blank=True,default=True)
	is_delete = models.BooleanField(default=False)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('ise_id', 'email',)

	def __str__(self):
		return self.name

class SMTPConfig(models.Model):
	
	email_host = models.CharField(max_length=255)
	email_host_user = models.TextField(default='',null=True)
	email_host_password = models.CharField(max_length=255)
	email_port = models.IntegerField(null=False)
	from_mail = models.CharField(max_length=255)
	enable_authentication = models.BooleanField(blank=True,default=False)
	use_ssl_tl = models.BooleanField(blank=True,default=False)