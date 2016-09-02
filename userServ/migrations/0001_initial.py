# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Falimy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(default=b'', max_length=255, verbose_name='\u5bb6\u5ead\u7535\u8bdd')),
            ],
            options={
                'verbose_name': '\u5bb6\u5ead',
                'verbose_name_plural': '\u5bb6\u5ead',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(default=0, verbose_name='\u5e74\u9f84')),
                ('sex', models.IntegerField(default=0, verbose_name='\u6027\u522b')),
                ('mobile', models.CharField(max_length=255, null=True, verbose_name='\u624b\u673a', blank=True)),
                ('member_type', models.IntegerField(default=0, verbose_name='\u6210\u5458\u7c7b\u522b')),
                ('belonged_falimy', models.ForeignKey(related_name='member_falimy', verbose_name='\u5bb6\u5ead', to='userServ.Falimy')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecifyVocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specify_voice_index', models.IntegerField(default=0, verbose_name='\u79d1\u5927\u8baf\u98de\u8bed\u97f3\u7f16\u53f7')),
                ('belonged_falimy', models.ForeignKey(related_name='voice_falimy', verbose_name='\u5bb6\u5ead', to='userServ.Falimy')),
            ],
            options={
                'verbose_name': '\u5bb6\u5ead\u53d1\u97f3\u97f3\u8272',
                'verbose_name_plural': '\u5bb6\u5ead\u53d1\u97f3\u97f3\u8272',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WakeupWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(default=b'', max_length=255, verbose_name='\u5524\u9192\u8bcd\u8bed')),
                ('specify_voice', models.ForeignKey(verbose_name='\u5524\u9192\u58f0\u97f3', to='userServ.SpecifyVocal')),
            ],
            options={
                'verbose_name': '\u5524\u9192\u8bcd',
                'verbose_name_plural': '\u5524\u9192\u8bcd',
            },
            bases=(models.Model,),
        ),
    ]
