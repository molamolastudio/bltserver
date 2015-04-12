# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0005_auto_20150407_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummy',
            name='friends',
            field=models.ManyToManyField(to='biolife.Dummy'),
            preserve_default=True,
        ),
    ]
