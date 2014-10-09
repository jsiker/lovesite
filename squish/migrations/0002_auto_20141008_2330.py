# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squish', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='dater',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='dater',
            name='city',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dater',
            name='country',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
