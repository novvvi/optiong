from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.quotes),
    url(r'^addqoutes$', views.quotes_add),
    url(r'^likes/(?P<user_id>\d+)/(?P<quotes_id>\d+)$', views.quotes_likes),
    url(r'^unlikes/(?P<user_id>\d+)/(?P<quotes_id>\d+)$', views.quotes_unlikes),
]