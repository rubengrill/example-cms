# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-08 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('tkdgarching', '0002_auto_20161208_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='tkdgarching_eventpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tkdgarching.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]