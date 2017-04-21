# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dssWeb', '0003_auto_20170416_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consignment',
            name='arrivalTime',
        ),
        migrations.RemoveField(
            model_name='consignment',
            name='departureTime',
        ),
        migrations.AddField(
            model_name='consignment',
            name='arrivingAt',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='consignment',
            name='departingAt',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
