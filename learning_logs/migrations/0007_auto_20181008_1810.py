# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-08 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_auto_20181007_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.NullBooleanField(default=False),
        ),
    ]