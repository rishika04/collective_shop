# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-09 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collective_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='PIN',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]