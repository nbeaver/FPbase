# Generated by Django 2.0.6 on 2018-06-29 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0012_auto_20180629_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microscope',
            name='configs',
            field=models.ManyToManyField(blank=True, related_name='collection_memberships', to='proteins.OpticalConfig'),
        ),
    ]