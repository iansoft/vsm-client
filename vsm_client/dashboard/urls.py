from django.conf.urls import include, url
from dashboard import views as dashboard_views
urlpatterns = [
    url(r'^$', dashboard_views.index,name="homepage"),
]