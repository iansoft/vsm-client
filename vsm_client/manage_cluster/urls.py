from django.conf.urls import include, url
from manage_cluster import views as cluster_views
urlpatterns = [
    url(r'^$', cluster_views.index,name="index"),
]