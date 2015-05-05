# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150505_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': '\u6807\u7b7e',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '\u7c7b\u578b'},
        ),
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 5, 47, 38, 983940), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 5, 47, 38, 983966), auto_now=True),
            preserve_default=True,
        ),
    ]
