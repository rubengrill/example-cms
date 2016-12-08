# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from parler.models import TranslatableModel, TranslatedFields


class Person(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        slug=models.SlugField(),
        content=HTMLField(),
        meta={'unique_together': [('language_code', 'slug')]},
    )

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.name


class Event(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        content=HTMLField(),
    )
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title
