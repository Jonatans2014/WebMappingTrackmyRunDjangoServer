# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0008_remove_location_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='distance',
            field=models.CharField(default=0, max_length=50),
        ),
    ]