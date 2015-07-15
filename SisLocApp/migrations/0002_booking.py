# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SisLocApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_init', models.DateTimeField()),
                ('creation_date', models.DateTimeField()),
                ('customer', models.ForeignKey(to='SisLocApp.Customers')),
                ('features', models.ManyToManyField(to='SisLocApp.Features')),
                ('user', models.ForeignKey(to='SisLocApp.Users')),
            ],
        ),
    ]
