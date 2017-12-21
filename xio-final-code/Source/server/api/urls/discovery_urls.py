from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.discovery_views import Discovery

urlpatterns = [
    url(r'^$', Discovery.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
