# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0014_auto_20150414_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='individual',
            field=models.ForeignKey(null=True, blank=True, to='biolife.Individual'),
            preserve_default=True,
        ),
    ]
