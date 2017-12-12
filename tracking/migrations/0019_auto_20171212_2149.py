# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0018_auto_20171212_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tracking.location'),
        ),
    ]
