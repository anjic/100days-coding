from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

	groups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = User
		fields = ('id','first_name','last_name','username','email','is_active','is_staff','groups')