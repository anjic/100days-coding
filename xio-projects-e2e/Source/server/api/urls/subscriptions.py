from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.subscriptions import(SubscriptionsList, SubscriptionsDetails)

urlpatterns = [
    url(r'^ise/(?P<ise_id>[\w\-]+)/subscriptions/$', SubscriptionsList.as_view()),
    url(r'^ise/(?P<ise_id>[\w\-]+)/subscriptions/(?P<sub_id>[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,4}\] | [\w\-]+)/(?P<type>[\w\-]+)$', SubscriptionsDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
