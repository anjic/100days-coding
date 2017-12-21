from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.snmp import(SnmpList, SnmpUpdate, SnmpClientDelete, SnmpClient)

urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/snmp/$', SnmpList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/snmp-client/$', SnmpClient.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/snmp-delete/$', SnmpClientDelete.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/snmp-update/$', SnmpUpdate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
