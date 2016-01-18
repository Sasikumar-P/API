# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fform', '0003_auto_20160112_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
