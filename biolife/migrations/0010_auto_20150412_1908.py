# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biolife', '0009_auto_20150412_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('location', models.TextField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_biolife_location_set')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='updated_biolife_location_set')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('weather', models.TextField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_biolife_weather_set')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='updated_biolife_weather_set')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='behaviour',
            name='ethogram',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='project',
        ),
        migrations.AddField(
            model_name='ethogram',
            name='behaviours',
            field=models.ManyToManyField(to='biolife.Behaviour'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='individuals',
            field=models.ManyToManyField(to='biolife.Individual'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='behaviour',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='biolife.Photo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='individual',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='biolife.Photo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='observation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='biolife.Location', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='observation',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='biolife.Photo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='observation',
            name='weather',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='biolife.Weather', null=True),
            preserve_default=True,
        ),
    ]
