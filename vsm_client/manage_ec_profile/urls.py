from django.conf.urls import include, url
from manage_ec_profile import views as ec_profile_views
urlpatterns = [
    url(r'^$', ec_profile_views.index,name="index"),
]