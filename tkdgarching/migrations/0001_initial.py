# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-08 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PersonTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('content', djangocms_text_ckeditor.fields.HTMLField()),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='tkdgarching.Person')),
            ],
            options={
                'managed': True,
                'db_table': 'tkdgarching_person_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'person Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='persontranslation',
            unique_together=set([('language_code', 'master'), ('language_code', 'slug')]),
        ),
    ]
