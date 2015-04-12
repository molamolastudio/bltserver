# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biolife', '0004_auto_20150329_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stringProperty', models.TextField()),
                ('intProperty', models.IntegerField()),
                ('dateProperty', models.DateTimeField()),
                ('optionalStringProperty', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='behaviour',
            name='information',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ethogram',
            name='information',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
