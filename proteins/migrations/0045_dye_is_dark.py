# Generated by Django 2.1.2 on 2018-12-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0044_auto_20181218_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='dye',
            name='is_dark',
            field=models.BooleanField(default=False, help_text='This state does not fluorescence', verbose_name='Dark State'),
        ),
    ]
