# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 01:06
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailySystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='messageContent',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
