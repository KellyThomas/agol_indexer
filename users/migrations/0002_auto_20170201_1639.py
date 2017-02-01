# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='comments',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
