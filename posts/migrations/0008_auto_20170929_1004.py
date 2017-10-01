# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-29 09:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 9, 29, 9, 4, 25, 757744, tzinfo=utc)),
            preserve_default=False,
        ),
    ]