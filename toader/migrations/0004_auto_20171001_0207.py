# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toader', '0003_remove_people_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='fullname',
            field=models.CharField(default='', max_length=200),
        ),
    ]