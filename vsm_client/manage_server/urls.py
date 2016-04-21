from django.conf.urls import include, url
from manage_server import views as server_views
urlpatterns = [
    url(r'^$', server_views.index,name="index"),
    url(r'^detail/(?P<id>\w+)/$', server_views.detail_view,name="detail"),
    url(r'^add/$', server_views.add_view,name="add"),
]