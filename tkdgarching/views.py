# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView, ListView
from parler.views import TranslatableSlugMixin

from tkdgarching import models


class NeverCacheMixin(object):

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(NeverCacheMixin, self).dispatch(*args, **kwargs)


class PersonListView(ListView):
    template_name = 'tkdgarching/person_list.html'
    queryset = models.Person.objects.all()


class PersonDetailView(TranslatableSlugMixin, DetailView):
    template_name = 'tkdgarching/person_detail.html'
    queryset = models.Person.objects.all()
