# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beaconQuest', '0003_auto_20161029_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountschallenges',
            name='beacon',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='accountschallenges',
            name='state',
            field=models.CharField(max_length=200),
        ),
    ]
