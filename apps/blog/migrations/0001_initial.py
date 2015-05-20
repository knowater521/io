# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(default=b'anonymous', max_length=128)),
                ('create_date', models.DateField()),
                ('modify_date', models.DateField(auto_now=True)),
                ('text', django_markdown.models.MarkdownField(null=True)),
                ('is_publish', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('desc', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'verbose_name_plural': '\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
