# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-27 01:11
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
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 27, 1, 11, 22, 19024, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
