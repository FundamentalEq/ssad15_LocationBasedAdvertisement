# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 12:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_auto_20161027_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadadvetisement',
            name='start_week',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 28, 12, 27, 56, 717961, tzinfo=utc), verbose_name='Starting week of the advertisement'),
        ),
    ]
