# Generated by Django 2.1.2 on 2019-01-03 14:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0004_auto_20181026_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='year',
            field=models.PositiveIntegerField(help_text='YYYY', validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.MinValueValidator(1960), django.core.validators.MaxValueValidator(2020)]),
        ),
    ]
