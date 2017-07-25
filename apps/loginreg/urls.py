from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^/verify', views.verify),
    url(r'^$', views.index),

]
