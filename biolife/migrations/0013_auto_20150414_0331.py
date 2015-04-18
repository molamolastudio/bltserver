# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0012_auto_20150413_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='session',
            field=models.ForeignKey(null=True, to='biolife.Session'),
            preserve_default=True,
        ),
    ]
