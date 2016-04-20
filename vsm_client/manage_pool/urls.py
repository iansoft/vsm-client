from django.conf.urls import include, url
from manage_pool import views as pool_views
urlpatterns = [
    url(r'^$', pool_views.index,name="index"),
]