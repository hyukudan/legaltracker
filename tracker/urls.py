# -*- coding: utf-8 -*-


from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^changelist/', include('changelist.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, {'template_name': 'login.html'}),
]


admin.site.site_header = 'Administración Tracker Legal'

