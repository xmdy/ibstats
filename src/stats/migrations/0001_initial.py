# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_created=True, db_index=True, verbose_name='time')),
                ('amount', models.FloatField(default=0.0, verbose_name='amount')),
                ('result_amount', models.FloatField(default=0.0, verbose_name='result amount')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'deal',
                'verbose_name_plural': 'deals',
            },
        ),
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('balance', models.FloatField(default=0.0, verbose_name='balance')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'trader',
                'verbose_name_plural': 'traders',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_created=True, verbose_name='time')),
                ('amount', models.FloatField(default=0.0, verbose_name='amount')),
                ('type', models.IntegerField(db_index=True, default=1, verbose_name='type')),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.Trader', verbose_name='trader')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
            },
        ),
        migrations.AddField(
            model_name='deal',
            name='trader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.Trader', verbose_name='trader'),
        ),
    ]