from django.conf.urls import include, url
from manage_storage_group import views as storage_group_views
urlpatterns = [
    url(r'^$', storage_group_views.index,name="index"),
]