# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0016_session_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethogram',
            name='behaviours',
            field=models.ManyToManyField(blank=True, to='biolife.Behaviour', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='individual',
            name='tags',
            field=models.ManyToManyField(blank=True, to='biolife.Tag', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='admins',
            field=models.ManyToManyField(related_name='administered_project_set', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='individuals',
            field=models.ManyToManyField(blank=True, to='biolife.Individual', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='joined_project_set', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
