# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userServ', '0002_memberface_membervocalprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='falimy',
            name='android_id',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u5b89\u5353ID'),
            preserve_default=True,
        ),
    ]
