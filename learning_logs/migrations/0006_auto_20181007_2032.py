# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-07 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_auto_20181007_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.NullBooleanField(),
        ),
    ]
