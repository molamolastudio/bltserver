# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0011_session_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weather',
            name='weather',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
