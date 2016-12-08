# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.conf.urls import url

from tkdgarching import views


@apphook_pool.register
class PersonApphook(CMSApp):
    name = 'Persons'
    urls = [
        [
            url(r'^$', views.PersonListView.as_view(), name='person-list'),
            url(r'^(?P<slug>[^/]+)/$', views.PersonDetailView.as_view(), name='person-detail'),
        ],
    ]
