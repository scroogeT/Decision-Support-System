# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dssWeb', '0009_auto_20170416_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='importedorders',
            name='arrivingAt',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='importedorders',
            name='deliveryStatus',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='dssWeb.deliveryState'),
        ),
        migrations.AddField(
            model_name='importedorders',
            name='departingAt',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='importedorders',
            name='isDelivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='importedorders',
            name='isReceived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='importedorders',
            name='tripNumber',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
