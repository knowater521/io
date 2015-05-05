# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150505_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=123, unique=True, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 5, 53, 42, 449382), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 5, 53, 42, 449412), auto_now=True),
            preserve_default=True,
        ),
    ]
