# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150506_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=django_markdown.models.MarkdownField(null=True),
        ),
    ]
