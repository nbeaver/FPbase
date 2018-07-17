# Generated by Django 2.0.6 on 2018-07-08 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proteins', '0011_auto_20180525_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='statetransition',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statetransition_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='statetransition',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statetransition_modifier', to=settings.AUTH_USER_MODEL),
        ),
    ]