# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0003_auto_20150329_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='information',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='observation',
            name='location',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='observation',
            name='weather',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
