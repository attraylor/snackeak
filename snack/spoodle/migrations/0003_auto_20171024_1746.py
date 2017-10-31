# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spoodle', '0002_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='classes',
        ),
        migrations.AddField(
            model_name='class',
            name='end',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='professor',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='spoodle.Professor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='start',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]