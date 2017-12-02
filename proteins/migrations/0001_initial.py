# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 20:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import proteins.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FRETpair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'FRET Pair',
            },
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_id', models.CharField(help_text='Enter the NCBI Taxonomy ID (e.g. 6100 for Aequorea victora) and the info will be retrieved automatically', max_length=8, verbose_name='Taxonomy ID')),
                ('scientific_name', models.CharField(blank=True, max_length=128)),
                ('division', models.CharField(blank=True, max_length=128)),
                ('common_name', models.CharField(blank=True, max_length=128)),
                ('species', models.CharField(blank=True, max_length=128)),
                ('genus', models.CharField(blank=True, max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organism_author', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organism_modifiers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Organism',
            },
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Enter the name of the protein (required)', max_length=128)),
                ('slug', models.SlugField(help_text='URL slug for the protein', max_length=64, unique=True)),
                ('base_name', models.CharField(max_length=128)),
                ('seq', models.CharField(blank=True, help_text='Amino acid sequence', max_length=512)),
                ('gb_prot', models.CharField(blank=True, help_text='Enter the GenBank protein Accession number (e.g. AFR60231) and the sequence will be retrieved automatically', max_length=10, null=True)),
                ('gb_nuc', models.CharField(blank=True, max_length=10, null=True)),
                ('mw', models.DecimalField(blank=True, decimal_places=2, help_text='Molecular Weight', max_digits=5, null=True)),
                ('agg', models.CharField(blank=True, choices=[('m', 'Monomer'), ('d', 'Dimer'), ('td', 'Tandem dimer'), ('wd', 'Weak dimer'), ('t', 'Tetramer')], help_text='Oligomerization tendency', max_length=2)),
                ('switch_type', models.CharField(blank=True, choices=[('b', 'Basic'), ('pa', 'Photoactivatable'), ('ps', 'Photoswitchable'), ('pc', 'Photoconvertible'), ('t', 'Timer'), ('o', 'Other')], help_text='Photoswitching type (basic if none)', max_length=2, verbose_name='Type')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blurb', models.CharField(blank=True, help_text='Brief descriptive blurb', max_length=512)),
                ('FRET_partner', models.ManyToManyField(blank=True, through='proteins.FRETpair', to='proteins.Protein')),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proteins_author', to=settings.AUTH_USER_MODEL)),
                ('additional_references', models.ManyToManyField(blank=True, related_name='FK_additionalReferences_reference', to='references.Reference', verbose_name='Additional References')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=128)),
                ('state_id', models.CharField(max_length=128)),
                ('default', models.BooleanField(default=False, help_text='Check if this is the default (basal) state for the protein')),
                ('ex_max', models.IntegerField(blank=True, null=True)),
                ('em_max', models.IntegerField(blank=True, null=True)),
                ('ex_spectra', proteins.models.SpectrumField(blank=True, help_text='Enter spectrum information as a list of [wavelength, value] pairs, e.g. [[300, 0.5],[301, 0.6] ... ]', null=True)),
                ('em_spectra', proteins.models.SpectrumField(blank=True, help_text='Enter spectrum information as a list of [wavelength, value] pairs, e.g. [[300, 0.5],[301, 0.6] ... ]', null=True)),
                ('ext_coeff', models.IntegerField(blank=True, help_text='Extinction Coefficient', null=True)),
                ('qy', models.DecimalField(blank=True, decimal_places=3, help_text='Quantum Yield', max_digits=4, null=True)),
                ('pka', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='pKa')),
                ('bleach_wide', models.DecimalField(blank=True, decimal_places=1, help_text='Widefield photobleaching rate', max_digits=5, null=True, verbose_name='Bleach Widefield')),
                ('bleach_conf', models.DecimalField(blank=True, decimal_places=1, help_text='Confocal photobleaching rate', max_digits=5, null=True, verbose_name='Bleach Confocal')),
                ('maturation', models.DecimalField(blank=True, decimal_places=1, help_text='Maturation time (seconds)', max_digits=4, null=True)),
                ('lifetime', models.DecimalField(blank=True, decimal_places=2, help_text='Fluorescence Lifetime (nanoseconds)', max_digits=3, null=True)),
                ('trans_wave', models.IntegerField(blank=True, help_text="Wavelength of light that drives the protein into the 'To state:' (if applicable)", null=True, verbose_name='Transition Wavelength')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_author', to=settings.AUTH_USER_MODEL)),
                ('protein', models.ForeignKey(help_text='The protein to which this state belongs', on_delete=django.db.models.deletion.CASCADE, related_name='states', to='proteins.Protein')),
                ('to_state', models.ForeignKey(blank=True, help_text="The state to which this state transitions upon 'transition wavelength' illumination", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transition_state', to='proteins.State', verbose_name='To state')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_modifiers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'State',
            },
        ),
        migrations.AddField(
            model_name='protein',
            name='default_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_state', to='proteins.State'),
        ),
        migrations.AddField(
            model_name='protein',
            name='parent_organism',
            field=models.ForeignKey(blank=True, help_text='Organism from which the protein was engineered', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parental_organism', to='proteins.Organism', verbose_name='Parental organism'),
        ),
        migrations.AddField(
            model_name='protein',
            name='primary_reference',
            field=models.ForeignKey(blank=True, help_text='Preferably the publication that introduced the protein', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='FK_primaryReference_reference', to='references.Reference', verbose_name='Primary Reference'),
        ),
        migrations.AddField(
            model_name='protein',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proteins_modifiers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fretpair',
            name='acceptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_FRETacceptor_protein', to='proteins.Protein', verbose_name='acceptor'),
        ),
        migrations.AddField(
            model_name='fretpair',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FRETpair_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fretpair',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_FRETdonor_protein', to='proteins.Protein', verbose_name='donor'),
        ),
        migrations.AddField(
            model_name='fretpair',
            name='pair_references',
            field=models.ManyToManyField(blank=True, related_name='FK_FRETpair_reference', to='references.Reference'),
        ),
        migrations.AddField(
            model_name='fretpair',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FRETpair_modifiers', to=settings.AUTH_USER_MODEL),
        ),
    ]