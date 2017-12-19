from __future__ import unicode_literals

from django.db import models


class SanGroup(models.Model):
	"""
	To store san details
	"""
	sangroup_id = models.AutoField(primary_key=True)
	sangroup_name = models.CharField(max_length=255,unique=True)
	comment = models.TextField(blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	created_by = models.CharField(max_length=255)
	modified_by = models.CharField(max_length=255)
	is_delete = models.BooleanField(default=False)

	# class Meta:
	# 	ordering = ('created_date')
	# 	db_table = 'san_group'

	def __str__(self):
		return self.sangroup_id

class SanIse(models.Model):
	"""
	To store san and ise link details
	"""
	sanise_id = models.AutoField(primary_key=True)
	san_id = models.IntegerField(blank=False)
	ise_id  = models.IntegerField(blank=False)
	is_delete = models.BooleanField(default=False)
	time_stamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('time_stamp',)
		db_table = 'san_ise'

	def __str__(self):
		return self.san_id




