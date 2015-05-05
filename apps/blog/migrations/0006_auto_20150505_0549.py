# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150505_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 5, 49, 55, 161854), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 5, 49, 55, 161902), auto_now=True),
            preserve_default=True,
        ),
    ]
