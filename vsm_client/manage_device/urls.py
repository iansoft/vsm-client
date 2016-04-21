from django.conf.urls import include, url
from manage_device import views as device_views
urlpatterns = [
    url(r'^$', device_views.index,name="index"),
    url(r'^add/$', device_views.add_view,name="add"),
    url(r'^import/$', device_views.import_view,name="import"),
]