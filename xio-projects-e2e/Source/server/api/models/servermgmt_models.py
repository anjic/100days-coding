from __future__ import unicode_literals

from django.db import models

from api.models.sangroup_models import SanGroup
from api.models.ise_models import ListIse

class ServerMgmt(models.Model):
	"""
	To store ServerMgmt details
	"""
	server_id = models.AutoField(primary_key=True)
	server_name = models.CharField(max_length=255,unique=True)
	comment = models.TextField(blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	created_by = models.CharField(max_length=255)
	modified_by = models.CharField(max_length=255)
	is_delete = models.BooleanField(default=False)


	def __str__(self):
		return self.server_id

class SangroupServer(models.Model):
	"""
		To save sangroup id mapped with server id
	"""
	id = models.AutoField(primary_key=True)
	san_id = models.ForeignKey(SanGroup, on_delete=models.CASCADE)
	server_id = models.ForeignKey(ServerMgmt,on_delete=models.CASCADE)
	time_stamp = models.DateTimeField(auto_now_add=True)

class ServerWwnIse(models.Model):
	"""
		To save wwngroup mapped with iseid and serverid
	"""
	id = models.AutoField(primary_key=True)
	server_id = models.ForeignKey(ServerMgmt,on_delete=models.CASCADE)
	ise_id = models.ForeignKey(ListIse,on_delete=models.CASCADE)
	wwngroup = models.CharField(max_length=255)