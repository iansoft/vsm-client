from django.conf.urls import include, url
from i18n_demo import views as i18n_views
urlpatterns = [
    url(r'^$', i18n_views.index,name="index"),
]