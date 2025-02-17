# Generated by Django 2.1.2 on 2018-11-07 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proteins', '0032_auto_20181107_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineage',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lineage_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lineage',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lineage_modifier', to=settings.AUTH_USER_MODEL),
        ),
    ]
