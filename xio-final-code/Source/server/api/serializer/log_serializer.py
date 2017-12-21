from rest_framework import serializers
from api.models.ise_models import MgmtLogs,EventLogs,MappingTable

class MgmtLogsSerializer(serializers.ModelSerializer):

	class Meta:
		model = MgmtLogs

class EventLogsSerializer(serializers.ModelSerializer):

	class Meta:
		model = EventLogs

class MappingTableSerializer(serializers.ModelSerializer):

	class Meta:
		model = MappingTable
