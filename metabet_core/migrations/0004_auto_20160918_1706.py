# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metabet_core', '0003_auto_20160917_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='competition',
        ),
        migrations.AddField(
            model_name='match',
            name='competition_season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metabet_core.CompetitionSeason'),
            preserve_default=False,
        ),
    ]
