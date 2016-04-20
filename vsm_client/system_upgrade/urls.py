from django.conf.urls import include, url
from system_upgrade import views as upgrade_views
urlpatterns = [
    url(r'^$', upgrade_views.index,name="index"),
]