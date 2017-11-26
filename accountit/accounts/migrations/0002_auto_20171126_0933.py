# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-26 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.Company'),
        ),
    ]
