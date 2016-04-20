from django.conf.urls import include, url
from manage_rbd import views as rbd_views
urlpatterns = [
    url(r'^$', rbd_views.index,name="index"),
]