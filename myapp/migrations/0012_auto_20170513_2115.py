# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-13 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20170512_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='content',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_target',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='content_report',
            field=models.CharField(max_length=1000),
        ),
    ]
