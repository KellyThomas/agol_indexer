# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Layer_Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50, verbose_name='Location or Database')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Layer Source',
            },
        ),
        migrations.CreateModel(
            name='Layer_Source_Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formats', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Layer Source Format',
            },
        ),
        migrations.CreateModel(
            name='Layer_Source_Format_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format_type', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Layer Source Format Type',
            },
        ),
        migrations.AddField(
            model_name='layer_source',
            name='feature_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layer_source.Layer_Source_Format_Type'),
        ),
        migrations.AddField(
            model_name='layer_source',
            name='formats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layer_source.Layer_Source_Format', verbose_name='format'),
        ),
    ]
