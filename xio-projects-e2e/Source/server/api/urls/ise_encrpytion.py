from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.ise_encryption import ISE_Encryption

urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/encryption/$', ISE_Encryption.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)