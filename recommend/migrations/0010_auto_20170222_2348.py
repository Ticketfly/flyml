# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 23:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0009_auto_20170222_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='similarusers',
            old_name='userqfvv',
            new_name='similar',
        ),
        migrations.RenameField(
            model_name='similarusers',
            old_name='similarqqqq',
            new_name='user',
        ),
    ]
