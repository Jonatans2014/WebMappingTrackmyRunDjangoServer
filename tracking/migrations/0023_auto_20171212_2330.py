# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 23:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0022_auto_20171212_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='track',
        ),
        migrations.DeleteModel(
            name='image',
        ),
    ]