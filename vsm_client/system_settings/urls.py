from django.conf.urls import include, url
from system_settings import views as settings_views
urlpatterns = [
    url(r'^$', settings_views.index,name="index"),
]