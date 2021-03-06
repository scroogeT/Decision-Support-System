# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 19:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dssWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='importedOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custID', models.CharField(max_length=30, unique=True)),
                ('customerName', models.CharField(max_length=150)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='consignment',
            name='arrivalTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 16, 19, 5, 32, 648501)),
        ),
        migrations.AddField(
            model_name='consignment',
            name='departureTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 16, 19, 5, 32, 648436)),
        ),
        migrations.AddField(
            model_name='consignment',
            name='isReceived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='consignment',
            name='tripNumber',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consignment',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
