from rest_framework import serializers
from api.models.temp_ise_models import IseService


class IseServiceSerializer(serializers.ModelSerializer):

	class Meta:
		model = IseService
		
