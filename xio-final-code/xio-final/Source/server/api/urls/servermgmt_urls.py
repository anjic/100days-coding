from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.servermgmt import (ServerMgmtList, SanServerMap, ServerMgmtDetail)


urlpatterns = [
    # url(r'^(?P<id>[\w\-]+)/hosts/$', SanGroupHost.as_view()),
    url(r'^(?P<id>[\w\-]+)/$', ServerMgmtDetail.as_view()),
    url(r'^$', ServerMgmtList.as_view()),
    url(r'^(?P<id>[\w\-]+)/sanserver-map/$', SanServerMap.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)