# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pomodori', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pomodoro',
            old_name='author',
            new_name='user',
        ),
    ]