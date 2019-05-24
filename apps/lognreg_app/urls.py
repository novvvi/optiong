from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$', views.lognreg),
    url(r'^logout$', views.logout),
    url(r'^myaccount/(?P<id>\d+)$', views.myaccount),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^myaccount/update$', views.myaccount_update),
    url(r'^login/verify_login$', views.lognreg_login),
    url(r'^login/verify_register$', views.lognreg_register),
]
