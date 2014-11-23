# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 23, 22, 15, 2, 414966), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 23, 22, 15, 2, 414998), auto_now_add=True),
            preserve_default=True,
        ),
    ]
