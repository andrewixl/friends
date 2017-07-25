from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout$', views.logout),
    url(r'^addfriend/(?P<id>\d+)$', views.addfriendlogic),
    url(r'^addfriend$', views.addfriend),
    url(r'^currentfriends$', views.currentfriend),
    url(r'^deletefriend/(?P<id>\d+)$', views.deletefriend),
    url(r'^home$', views.index),

]
