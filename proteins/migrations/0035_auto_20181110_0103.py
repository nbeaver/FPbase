# Generated by Django 2.1.2 on 2018-11-10 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0034_lineage_rootmut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mutation',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Mutation',
        ),
    ]
