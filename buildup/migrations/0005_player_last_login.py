# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-25 20:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('buildup', '0004_auto_20160925_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 25, 20, 51, 17, 279550, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
