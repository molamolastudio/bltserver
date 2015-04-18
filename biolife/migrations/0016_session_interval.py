# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0015_auto_20150417_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='interval',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
