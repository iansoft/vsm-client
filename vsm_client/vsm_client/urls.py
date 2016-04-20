"""vsm_client URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', include('dashboard.urls')),
    url(r'^home/$', include('dashboard.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^cluster/', include('manage_cluster.urls')),
    url(r'^server/', include('manage_server.urls')),
    url(r'^device/', include('manage_device.urls')),
    url(r'^pool/', include('manage_pool.urls')),
    url(r'^ec_profile/', include('manage_ec_profile.urls')),
    url(r'^rbd/', include('manage_rbd.urls')),
    url(r'^crushmap/', include('manage_storage_group.urls')),
    url(r'^zone/', include('manage_zone.urls')),

    url(r'^performance/monitor/', include('performance_monitor.urls')),

    url(r'^integrate/hadoop/', include('integrate_hadoop.urls')),
    url(r'^integrate/openstack/', include('integrate_openstack.urls')),

    url(r'^settings/', include('system_settings.urls')),
    url(r'^account/', include('manage_account.urls')),
    url(r'^role/', include('manage_role.urls')),
    url(r'^upgrade/ceph/', include('system_upgrade.urls')),
]
