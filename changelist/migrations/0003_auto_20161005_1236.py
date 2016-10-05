# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changelist', '0002_contract'),
    ]

    operations = [
        migrations.CreateModel(
            name='articleLaw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=200)),
                ('version', models.IntegerField(default=0)),
                ('fromLaw', models.ForeignKey(to='changelist.Law')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'contrato', 'verbose_name_plural': 'contratos'},
        ),
        migrations.AddField(
            model_name='law',
            name='total_articles',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contract',
            name='applied_laws',
            field=models.ManyToManyField(to='changelist.articleLaw'),
            preserve_default=True,
        ),
    ]
