# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-02 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt2', '0002_auto_20180302_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
    ]
