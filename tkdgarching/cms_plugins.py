# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import get_language

from tkdgarching import models


@plugin_pool.register_plugin
class EventPlugin(CMSPluginBase):
    render_template = 'tkdgarching/plugins/event.html'

    def render(self, context, instance, placeholder):
        context = super(EventPlugin, self).render(context, instance, placeholder)
        context['event'] = (
            models.Event.objects
            .filter(translations__language_code=get_language())
            .order_by('-date')
            .first()
        )
        return context
