from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.wwn_groups import (WWNGroupList, WWNGroupCreate, WWNGroupDetail, WWNGroupUpdate, WWNGroupServer)

urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-,*]+)/wwngroups/$', WWNGroupList.as_view()),
    url(r'^servermgmt/(?P<server_id>[\w\-]+)/wwngroups/$', WWNGroupCreate.as_view()),
    url(r'^servermgmt/(?P<server_id>[\w\-]+)/wwnserver-map/$', WWNGroupUpdate.as_view()),
    url(r'^sangroup/(?P<san_id>[\w\-]+)/wwnserver/(?P<server_id>[\w\-]+)$', WWNGroupServer.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/wwngroups/(?P<wwngroup_id>[\w\-]+)/(?P<san_id>[\w\-]*)$', WWNGroupDetail.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
