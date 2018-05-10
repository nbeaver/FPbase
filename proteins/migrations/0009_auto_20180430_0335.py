# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-30 03:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0008_auto_20180430_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='tavg',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
    ]