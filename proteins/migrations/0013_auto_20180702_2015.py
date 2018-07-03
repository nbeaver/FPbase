# Generated by Django 2.0.6 on 2018-07-02 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proteins', '0012_auto_20180701_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='microscope',
            name='configs',
        ),
        migrations.AddField(
            model_name='opticalconfig',
            name='microscope',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='optical_configs', to='proteins.Microscope'),
            preserve_default=False,
        ),
    ]