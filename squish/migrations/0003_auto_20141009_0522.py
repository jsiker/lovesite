# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('squish', '0002_auto_20141008_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dater',
            name='user',
            field=models.OneToOneField(related_name=b'profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
