# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin


urlpatterns = i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)
