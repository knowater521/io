# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150602_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='text',
            field=django_markdown.models.MarkdownField(null=True),
        ),
    ]
