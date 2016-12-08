# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from parler.admin import TranslatableAdmin
from django.contrib import admin

from tkdgarching import models


@admin.register(models.Person)
class PersonAdmin(TranslatableAdmin):
    list_display = ('slug', 'name')
    search_fields = ('translations__name',)

    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
