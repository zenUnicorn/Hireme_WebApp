# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-09 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone_number',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='skill',
            field=models.CharField(max_length=200),
        ),
    ]