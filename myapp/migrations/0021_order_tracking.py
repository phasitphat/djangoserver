# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-28 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20170525_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tracking',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
