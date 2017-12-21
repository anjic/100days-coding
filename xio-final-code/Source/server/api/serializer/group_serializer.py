from rest_framework import serializers
from django.contrib.auth.models import Group, Permission


class GroupSerializer(serializers.ModelSerializer):

	class Meta:
		model = Group

class PermissionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Permission
