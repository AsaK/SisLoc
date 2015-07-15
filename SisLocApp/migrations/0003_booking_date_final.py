# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SisLocApp', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date_final',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 11, 31, 25, 393000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
