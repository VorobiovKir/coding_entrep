# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_uniquidid'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniquidid',
            name='content',
            field=models.CharField(default='apple', max_length=120, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uniquidid',
            name='name',
            field=models.CharField(max_length=120, primary_key=True),
        ),
    ]
