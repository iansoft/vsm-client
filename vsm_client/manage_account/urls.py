from django.conf.urls import include, url
from manage_account import views as account_views
urlpatterns = [
    url(r'^$', account_views.index,name="index"),
]