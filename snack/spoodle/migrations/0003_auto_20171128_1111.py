# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 16:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoodle', '0002_chatpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatpost',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
