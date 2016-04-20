from django.conf.urls import include, url
from integrate_openstack import views as openstack_views
urlpatterns = [
    url(r'^$', openstack_views.index,name="index"),
]