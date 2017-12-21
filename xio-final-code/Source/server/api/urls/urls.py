from django.conf.urls import url, include


from api.views.menu import Sidemenu
from api.views.mail import SendMail
from api.views.sangroup_views import SanIseDetail

urlpatterns = [
    
    # sidemenu details
    url(r'^menu-content/', Sidemenu.as_view()),

    # test mail send
    url(r'^mail/', SendMail.as_view()),

    # url(r'^node/$', views.NodeList.as_view()),
    # settings
    url(r'^', include('api.urls.settings')),

    # authentication
    url(r'^', include('api.urls.users_urls')),

    # Dashboard
    url(r'^', include('api.urls.array_urls')),
    # Discovery
    url(r'^discovery/', include('api.urls.discovery_urls')),

    # Ise CRUD
    url(r'^', include('api.urls.ise_urls')),

    # SanGroup CRUD
    url(r'^sangroup/', include('api.urls.sangroup_urls')),
    url(r'^san-ise/(?P<ise_id>[\w\-]+)/$', SanIseDetail.as_view()),

    # ServerMgmt CRUD
    url(r'^servermgmt/', include('api.urls.servermgmt_urls')),
    
    # Logical strorage resources
    url(r'^', include('api.urls.wwn_groups')),
    url(r'^', include('api.urls.volume_urls')),
    url(r'^', include('api.urls.host_urls')),
    url(r'^', include('api.urls.endpoint_urls')),
    url(r'^', include('api.urls.pool_urls')),
    url(r'^', include('api.urls.drive_urls')),

    # Physical System Resources
    url(r'^', include('api.urls.controllers')),
    url(r'^', include('api.urls.media')),
    url(r'^', include('api.urls.powersupplies')),
    url(r'^', include('api.urls.batteries')),

    # Logical System Resources
    url(r'^', include('api.urls.network')),
    url(r'^', include('api.urls.chronometer')),
    url(r'^', include('api.urls.fans')),
    url(r'^', include('api.urls.files')),
    url(r'^', include('api.urls.subscriptions')),
    url(r'^', include('api.urls.snmp')),
    url(r'^', include('api.urls.performance')),

    # Encryption 
    url(r'^', include('api.urls.ise_encrpytion')),

]
