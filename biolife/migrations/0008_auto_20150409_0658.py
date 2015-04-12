# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biolife', '0007_auto_20150409_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummy',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 9, 6, 57, 52, 695250, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dummy',
            name='created_by',
            field=models.ForeignKey(related_name='created_biolife_dummy_set', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dummy',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 9, 6, 58, 6, 902793, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dummy',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_biolife_dummy_set', to=settings.AUTH_USER_MODEL, default=2),
            preserve_default=False,
        ),
    ]
