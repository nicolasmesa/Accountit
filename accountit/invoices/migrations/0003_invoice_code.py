# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-27 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_itemsold_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='code',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
