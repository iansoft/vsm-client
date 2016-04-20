from django.conf.urls import include, url
from integrate_hadoop import views as hadoop_views
urlpatterns = [
    url(r'^$', hadoop_views.index,name="index"),
]