# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dssWeb', '0005_auto_20170416_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consignment',
            name='tripNumber',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='consignment',
            name='value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='consignment',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='importedorders',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='importedorders',
            name='long',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='truck',
            name='milleage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='truck',
            name='tonnage',
            field=models.IntegerField(default=0),
        ),
    ]
