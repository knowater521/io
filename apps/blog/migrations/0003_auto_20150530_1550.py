# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='modify_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
