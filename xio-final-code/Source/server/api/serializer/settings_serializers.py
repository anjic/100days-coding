from rest_framework import serializers
from api.models.settings import MailUser

class MailUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = MailUser
		fields = ('id','name','email','ise_id','is_active','normal','critical','severe','error','warning','informational',)
