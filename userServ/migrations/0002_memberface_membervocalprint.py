# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userServ', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberFace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('face_img_link', models.CharField(default=b'', max_length=255, verbose_name='\u4eba\u8138\u56fe\u7247\u94fe\u63a5\u5730\u5740')),
                ('predict_age', models.IntegerField(default=0, verbose_name='\u9884\u6d4b\u5e74\u9f84')),
                ('belonged_member', models.ForeignKey(related_name='member_face', verbose_name='\u6240\u5c5e\u6210\u5458', to='userServ.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemberVocalPrint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vocal_print_link', models.CharField(default=b'', max_length=255, verbose_name='\u58f0\u7eb9\u6570\u636e\u94fe\u63a5\u5730\u5740')),
                ('belonged_member', models.ForeignKey(related_name='member_vocal_print', verbose_name='\u6240\u5c5e\u6210\u5458', to='userServ.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
