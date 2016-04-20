from django.conf.urls import include, url
from performance_monitor import views as monitor_views
urlpatterns = [
    url(r'^$', monitor_views.index,name="index"),
]