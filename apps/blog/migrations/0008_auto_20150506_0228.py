# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150505_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=123, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 6, 2, 28, 23, 762782), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 6, 2, 28, 23, 762809), auto_now=True),
            preserve_default=True,
        ),
    ]
