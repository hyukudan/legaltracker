# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('changelist', '0006_auto_20161005_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='law',
            name='date_publication',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Versi\xc3\xb3n de fecha'),
        ),
    ]
