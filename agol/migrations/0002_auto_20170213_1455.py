# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agol_item',
            name='external_layer_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agol_item',
            name='mxd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mxd.MXD', verbose_name='External MXD'),
        ),
        migrations.AlterField(
            model_name='agol_item',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_service.Web_Service', verbose_name='External url'),
        ),
    ]
