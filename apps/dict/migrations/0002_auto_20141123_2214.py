# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dict',
            name='create_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 23, 22, 14, 33, 216744), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dict',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 23, 22, 14, 33, 216774), auto_now_add=True),
            preserve_default=True,
        ),
    ]
