# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 14:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0007_auto_20171212_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='photo',
        ),
    ]
