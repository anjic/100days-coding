from __future__ import unicode_literals

from django.db import models

# class Node(models.Model):
# 	"""
# 		To save node data
# 	"""
# 	id = models.AutoField(primary_key=True)
# 	parent_node_id = models.IntegerField(null=True)
# 	node_name = models.CharField(max_length=255,default='')
# 	node_value = models.CharField(max_length=255,default='')
# 	has_child = models.BooleanField(default=False)
# 	ts = models.DateTimeField(auto_now_add=True)


# class NodeAttribute(models.Model):
# 	"""
# 	   To save node attribute values
# 	"""
# 	id = models.AutoField(primary_key=True)
# 	# node_id = models.ForeignKey(Node, on_delete=models.CASCADE)
# 	node_id = models.IntegerField()
# 	attribute_name = models.CharField(max_length=255)
# 	attribute_value = models.CharField(max_length=255)
# 	ts = models.DateTimeField(auto_now_add=True)


	# def __str__(self):
	# 	return self.ise_name

class ListIse(models.Model):
	"""
		To save ise list details
	"""
	id = models.AutoField(primary_key=True)
	root_node_id = models.IntegerField(null=True)
	ise_name = models.CharField(max_length=255)
	raw_data = models.TextField()
	serial_no = models.TextField()
	ip_primary = models.TextField(default='', null=False)
	ip_secondary = models.TextField(default='', null=False)
	mrc1_status = models.BooleanField(default=True)
	mrc2_status = models.BooleanField(default=True)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	time_stamp = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(null=True)
	initialize = models.CharField(max_length=255, default=None, null=True)
	contactphone = models.CharField(max_length=255, default=None, null=True)
	contactemail = models.CharField(max_length=255, default=None, null=True)
	contactname = models.CharField(max_length=255, default=None, null=True)
	location = models.CharField(max_length=255, default=None, null=True)
	address = models.CharField(max_length=255, default=None, null=True)
	prefered = models.BooleanField(default=False)
	# def __str__(self):
	# 	return self.ise_name

class SangroupIse(models.Model):
	"""
		To save ise id mapped with sangroup id
	"""
	id = models.AutoField(primary_key=True)
	ise_id = models.IntegerField()
	sg_id = models.IntegerField()
	time_stamp = models.DateTimeField(auto_now_add=True)


class StorageCount(models.Model):
	"""
		To save ise list details
	"""
	id = models.AutoField(primary_key=True)
	ise_id = models.ForeignKey(ListIse,on_delete=models.CASCADE)
	pools = models.IntegerField()
	volumes = models.IntegerField()
	endpoints = models.IntegerField()
	hosts = models.IntegerField()
	modified_time = models.DateTimeField(auto_now=True)

class MgmtLogs(models.Model):
	"""
	To store san details

	{
                        "Status": 1,
                        "Code": 3061,
                        "Severity": "Normal",
                        "Service": "Config Manager",
                        "Object": 0,
                        "Time": "07:00:21 am",
                        "Date": "30-Mar-2017",
                        "Data": "Other MRC has joined.  Synching MGMT files.",
                        "Method": 0
                    }

	"""
	ise_id = models.ForeignKey(ListIse,on_delete=models.CASCADE)
	status = models.IntegerField(blank=True,null=False)
	code = models.IntegerField(blank=True,null=True)
	severity = models.CharField(max_length=255,blank=True,null=True)
	service = models.CharField(max_length=255,blank=True,null=True)
	date_time = models.DateTimeField(blank=True,null=True)
	data = models.CharField(max_length=1000,blank=True,null=True)
	is_sent = models.BooleanField(default=False)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('ise_id', 'code','date_time','data')

	def __str__(self):
		return self.ise_id

class EventLogs(models.Model):
	"""
	To store san details

	{
                        "Description": "CEL Event - Type: 231,  Component: CCS,  Class: 8, Sequence Num: 0.2c.e6  - A Volume has been presented to a host. Vol GUID: 6001F93104B000010CCF000200000000, Vol Index: 26, Host Index: 1,  Status: 00000005 - Volume busy",
                        "Component": "CCS",
                        "time": "06:20:57 am",
                        "date": "17-Apr-2017",
                        "Type": 231,
                        "Class": 8
                    }

	"""
	ise_id = models.ForeignKey(ListIse,on_delete=models.CASCADE)
	component = models.CharField(max_length=255,blank=True,null=True)
	event_type = models.IntegerField(blank=True,null=False)
	event_class = models.IntegerField(blank=True,null=True)
	date_time = models.DateTimeField(blank=True,null=True)
	description = models.CharField(max_length=1000,blank=True,null=True)
	is_sent = models.BooleanField(default=False)
	created_date = models.DateTimeField(auto_now_add=True)
	severity = models.CharField(max_length=255,blank=True,null=True)

	class Meta:
		unique_together = ('ise_id','component','event_type','event_class','date_time','description')

	def __str__(self):
		return self.ise_id

class MappingTable(models.Model):

	ise_id = models.ForeignKey(ListIse,on_delete=models.CASCADE)
	een_value = models.IntegerField(blank=True,null=False)
	severity = models.CharField(max_length=255,blank=True,null=True)

	class Meta:
		unique_together = ('ise_id','een_value','severity')

	# def __str__(self):
	# 	return self.ise_id