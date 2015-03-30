# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='behaviour',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='individual',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='observation',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
    ]
