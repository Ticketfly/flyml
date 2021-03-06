# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 02:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0002_auto_20170217_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventrecommendations',
            old_name='serial_event',
            new_name='event_dim_id',
        ),
        migrations.RenameField(
            model_name='eventrecommendations',
            old_name='serial_user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='similarevents',
            old_name='serial_event1',
            new_name='event1_dim_id',
        ),
        migrations.RenameField(
            model_name='similarevents',
            old_name='serial_event2',
            new_name='event2_dim_id',
        ),
        migrations.RenameField(
            model_name='similarusers',
            old_name='serial_user1',
            new_name='user1_dim_id',
        ),
        migrations.RenameField(
            model_name='similarusers',
            old_name='serial_user2',
            new_name='user2_dim_id',
        ),
        migrations.RenameField(
            model_name='userrecommendations',
            old_name='serial_user',
            new_name='event_dim_id',
        ),
        migrations.RenameField(
            model_name='userrecommendations',
            old_name='series_event',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='serial',
        ),
        migrations.RemoveField(
            model_name='user',
            name='serial',
        ),
    ]
