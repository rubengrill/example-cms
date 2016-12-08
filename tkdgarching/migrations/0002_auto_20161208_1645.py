# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-08 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('tkdgarching', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EventTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255)),
                ('content', djangocms_text_ckeditor.fields.HTMLField()),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='tkdgarching.Event')),
            ],
            options={
                'managed': True,
                'db_table': 'tkdgarching_event_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'event Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='eventtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]