# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dssWeb', '0010_auto_20170417_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importedorders',
            name='deliveryStatus',
            field=models.ForeignKey(blank=True, default=4, on_delete=django.db.models.deletion.CASCADE, to='dssWeb.deliveryState'),
        ),
    ]
