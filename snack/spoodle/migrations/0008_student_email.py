# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoodle', '0007_auto_20171031_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, primary_key=True),
            preserve_default=False,
        ),
    ]
