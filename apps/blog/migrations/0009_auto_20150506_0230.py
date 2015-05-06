# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150506_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 6, 2, 30, 27, 832543), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 6, 2, 30, 27, 832589), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
