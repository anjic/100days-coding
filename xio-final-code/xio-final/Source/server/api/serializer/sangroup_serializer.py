from rest_framework import serializers
from api.models.sangroup_models import SanGroup, SanIse


class SanGroupSerializer(serializers.ModelSerializer):

	class Meta:
		model = SanGroup
