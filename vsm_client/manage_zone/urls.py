from django.conf.urls import include, url
from manage_zone import views as zone_views
urlpatterns = [
    url(r'^$', zone_views.index,name="index"),
]