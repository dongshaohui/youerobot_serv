# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userServ', '0004_productvocal'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductWakeWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wake_up_word_index', models.IntegerField(default=0, verbose_name='\u79d1\u5927\u8baf\u98de\u5524\u9192\u8bcd\u7f16\u53f7')),
            ],
            options={
                'verbose_name': '\u79d1\u5927\u8baf\u98de\u5524\u9192\u8bcd\u7f16\u53f7',
                'verbose_name_plural': '\u79d1\u5927\u8baf\u98de\u5524\u9192\u8bcd\u7f16\u53f7',
            },
            bases=(models.Model,),
        ),
    ]
