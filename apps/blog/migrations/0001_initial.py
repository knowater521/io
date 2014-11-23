# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_timestamp', models.DateTimeField(default=True, auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(default=True, auto_now_add=True)),
                ('title', models.CharField(default=b'title', max_length=64)),
                ('is_published', models.BooleanField(default=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
