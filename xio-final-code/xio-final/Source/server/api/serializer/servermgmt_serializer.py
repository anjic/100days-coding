from rest_framework import serializers
from api.models.servermgmt_models import ServerMgmt


class ServerMgmtSerializer(serializers.ModelSerializer):

	class Meta:
		model = ServerMgmt