from django.conf.urls import include, url
from manage_pool import views as pool_views
urlpatterns = [
    url(r'^$', pool_views.index,name="index"),
    url(r'^create_replicated_pool/$', pool_views.create_replicated_pool_view,name="create_replicated_pool"),
    url(r'^create_ec_pool/$', pool_views.create_ec_pool_view,name="create_ec_pool"),
    url(r'^add_cache_tier/$', pool_views.add_cache_tier_view,name="add_cache_tier"),
]