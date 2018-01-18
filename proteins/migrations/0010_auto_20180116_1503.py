# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-16 15:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0009_auto_20180115_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='proteincollection',
            name='private',
            field=models.BooleanField(default=False, verbose_name='Make Private'),
        ),
        migrations.AlterField(
            model_name='state',
            name='maturation',
            field=models.FloatField(blank=True, help_text='Maturation time (min)', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1600)]),
        ),
    ]