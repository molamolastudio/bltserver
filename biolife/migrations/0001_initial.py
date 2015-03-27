# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Behaviour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('information', models.TextField()),
                ('created_by', models.ForeignKey(related_name='biolife_behaviour_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ethogram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('information', models.TextField()),
                ('created_by', models.ForeignKey(related_name='biolife_ethogram_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='biolife_ethogram_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(related_name='biolife_individual_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('information', models.TextField(default='')),
                ('timestamp', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('weather', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(related_name='biolife_observation_created', to=settings.AUTH_USER_MODEL)),
                ('individual', models.ForeignKey(to='biolife.Individual')),
                ('recorded_behaviour', models.ForeignKey(to='biolife.Behaviour')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('admins', models.ManyToManyField(related_name='projects_administered', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(related_name='biolife_project_created', to=settings.AUTH_USER_MODEL)),
                ('ethogram', models.ForeignKey(to='biolife.Ethogram', null=True)),
                ('members', models.ManyToManyField(related_name='projects_joined', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='biolife_project_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('session_type', models.CharField(max_length=3, default='SCN', choices=[('FCL', 'Focal Sampling'), ('SCN', 'Scan Sampling')])),
                ('created_by', models.ForeignKey(related_name='biolife_session_created', to=settings.AUTH_USER_MODEL)),
                ('individuals', models.ManyToManyField(to='biolife.Individual')),
                ('project', models.ForeignKey(to='biolife.Project')),
                ('updated_by', models.ForeignKey(related_name='biolife_session_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(related_name='biolife_tag_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='biolife_tag_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='observation',
            name='session',
            field=models.ForeignKey(to='biolife.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='observation',
            name='updated_by',
            field=models.ForeignKey(related_name='biolife_observation_updated', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='individual',
            name='project',
            field=models.ForeignKey(to='biolife.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='individual',
            name='tags',
            field=models.ManyToManyField(to='biolife.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='individual',
            name='updated_by',
            field=models.ForeignKey(related_name='biolife_individual_updated', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='behaviour',
            name='ethogram',
            field=models.ForeignKey(to='biolife.Ethogram'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='behaviour',
            name='updated_by',
            field=models.ForeignKey(related_name='biolife_behaviour_updated', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
