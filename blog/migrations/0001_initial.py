# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('category', models.CharField(blank=True, max_length=50)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]