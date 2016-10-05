# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameCompany', models.CharField(max_length=200)),
                ('NIF', models.CharField(max_length=10)),
                ('mail', models.CharField(default=b'info@localhost.com', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('area', models.CharField(default=b'CV', max_length=2, choices=[(b'CV', b'Civil'), (b'PN', b'Penal'), (b'SO', b'Social'), (b'AD', b'Administrativo')])),
                ('date_last_revision', models.DateTimeField(verbose_name=b'\xc3\x9altima modificaci\xc3\xb3n')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='textLaw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revision_text', models.CharField(max_length=200)),
                ('revision_date', models.DateTimeField(verbose_name=b'Actualizaci\xc3\xb3n de fecha')),
                ('law', models.ForeignKey(to='changelist.Law')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
