# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-09 14:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_remove_location_speed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='LongLat',
        ),
    ]
