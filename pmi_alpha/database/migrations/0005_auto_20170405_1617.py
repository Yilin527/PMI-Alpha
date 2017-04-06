# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20170328_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='Clearance',
            field=models.CharField(default=None, max_length=50, verbose_name='Clearance'),
        ),
        migrations.AddField(
            model_name='contract',
            name='ContractName',
            field=models.CharField(default=None, max_length=50, verbose_name='Contract Name'),
        ),
        migrations.AddField(
            model_name='contract',
            name='ContractType',
            field=models.CharField(choices=[('LH', 'Labor Hour'), ('T', 'TNM'), ('F', 'FFP')], default=None, max_length=50, verbose_name='Contract Type'),
        ),
        migrations.AddField(
            model_name='contract',
            name='ContractValue',
            field=models.CharField(default=None, max_length=50, verbose_name='Contract Value'),
        ),
        migrations.AddField(
            model_name='contract',
            name='PlaceOfPerformance',
            field=models.CharField(default=None, max_length=50, verbose_name='Place Of Performance'),
        ),
        migrations.AddField(
            model_name='contract',
            name='Scope',
            field=models.CharField(default=None, max_length=50, verbose_name='Scope'),
        ),
    ]
