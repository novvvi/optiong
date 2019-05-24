from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.lognreg_app.urls")),
    url(r'^quotes/', include("apps.optiong_app.urls")),
]