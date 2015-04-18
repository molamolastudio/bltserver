# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0013_auto_20150414_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='project',
            field=models.ForeignKey(null=True, to='biolife.Project'),
            preserve_default=True,
        ),
    ]
