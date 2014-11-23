# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_timestamp', models.DateTimeField(default=datetime.datetime(2014, 11, 23, 22, 14, 16, 479279), auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(default=datetime.datetime(2014, 11, 23, 22, 14, 16, 479311), auto_now_add=True)),
                ('english', models.CharField(default=b'english', max_length=128)),
                ('chinese', models.CharField(default=b'chinese', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
