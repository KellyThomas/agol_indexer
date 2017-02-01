# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Web_Adapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=20)),
                ('enviroment', models.CharField(max_length=4)),
                ('alias', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Web Adapter',
            },
        ),
    ]
