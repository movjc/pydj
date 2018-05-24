# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 08:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Criticism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criticismContent', models.TextField()),
                ('criticismTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeSex', models.CharField(max_length=10)),
                ('employeeBirth', models.DateField()),
                ('employeePhone', models.CharField(max_length=100)),
                ('employeePlace', models.TextField()),
                ('joinTime', models.DateField()),
                ('isLead', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageTitle', models.CharField(max_length=256)),
                ('messageContent', models.TextField()),
                ('publishTime', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailySystem.Employee')),
            ],
            options={
                'ordering': ('-publishTime',),
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replyContent', models.TextField()),
                ('replyTime', models.DateTimeField()),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailySystem.Employee')),
                ('messageID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailySystem.Message')),
            ],
        ),
        migrations.AddField(
            model_name='criticism',
            name='employeeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailySystem.Employee'),
        ),
        migrations.AddField(
            model_name='criticism',
            name='messageID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailySystem.Message'),
        ),
    ]
