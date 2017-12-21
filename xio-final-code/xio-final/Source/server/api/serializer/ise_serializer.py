from rest_framework import serializers
from api.models.ise_models import ListIse


class IseListSerializer(serializers.ModelSerializer):

	class Meta:
		model = ListIse
