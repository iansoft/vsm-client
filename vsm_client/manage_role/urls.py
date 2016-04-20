from django.conf.urls import include, url
from manage_role import views as role_views
urlpatterns = [
    url(r'^$', role_views.index,name="index"),
]