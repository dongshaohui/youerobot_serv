# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userServ', '0003_falimy_android_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voice_index', models.IntegerField(default=0, verbose_name='\u79d1\u5927\u8baf\u98de\u8bed\u97f3\u7f16\u53f7')),
            ],
            options={
                'verbose_name': '\u673a\u5668\u4eba\u51fa\u5382\u97f3\u8272\u7f16\u53f7',
                'verbose_name_plural': '\u673a\u5668\u4eba\u51fa\u5382\u97f3\u8272\u7f16\u53f7',
            },
            bases=(models.Model,),
        ),
    ]
