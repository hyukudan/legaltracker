# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('changelist', '0011_auto_20161005_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlelaw',
            name='version',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
