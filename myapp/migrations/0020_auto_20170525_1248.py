# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-25 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20170521_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_detail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_quantity',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
