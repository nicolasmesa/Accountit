# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-27 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0007_user_is_admin'),
        ('items', '0002_auto_20171127_0414'),
        ('contacts', '0002_auto_20171127_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('observations', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Company')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contacts.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='ItemSold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.FloatField()),
                ('tax', models.FloatField()),
                ('observations', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Company')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoices.Invoice')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.Item')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='items',
            field=models.ManyToManyField(through='invoices.ItemSold', to='items.Item'),
        ),
    ]
