# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-06 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_auto_20180903_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='public',
            field=models.NullBooleanField(default=False),
        ),
    ]
