# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(default=b'anonymous', max_length=100)),
                ('create_date', models.DateField(default=datetime.datetime(2015, 5, 4, 10, 20, 47, 591595), auto_now_add=True)),
                ('modify_date', models.DateField(default=datetime.datetime(2015, 5, 4, 10, 20, 47, 591619), auto_now=True)),
                ('content', models.TextField(default=b'')),
                ('is_publish', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
