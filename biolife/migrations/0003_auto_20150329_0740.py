# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0002_auto_20150327_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='behaviour',
            name='created_by',
            field=models.ForeignKey(related_name='created_biolife_behaviour_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='behaviour',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_biolife_behaviour_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ethogram',
            name='created_by',
            field=models.ForeignKey(related_name='created_biolife_ethogram_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ethogram',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_biolife_ethogram_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='individual',
            name='created_by',
            field=models.ForeignKey(related_name='created_biolife_individual_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='individual',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_biolife_individual_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='observation',
            name='created_by',
            field=models.ForeignKey(related_name='created_biolife_observation_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='observation',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_biolife_observation_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='admins',
            field=models.ManyToManyField(related_name='administered_project_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(related_name='created_biolife_project_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='ethogram',
            field=models.ForeignKey(null=True, blank=True, to='biolife.Ethogram'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='joined_project_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_biolife_project_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='session',
            name='created_by',
            field=models.ForeignKey(related_name='created_biolife_session_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='session',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_biolife_session_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_by',
            field=models.ForeignKey(related_name='created_biolife_tag_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_biolife_tag_set', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
