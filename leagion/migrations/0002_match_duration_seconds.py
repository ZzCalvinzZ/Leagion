# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-15 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='duration_seconds',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]