# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='display_title',
            field=models.CharField(max_length=140, null=True),
        ),
    ]