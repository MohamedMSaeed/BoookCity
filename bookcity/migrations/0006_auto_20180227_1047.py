# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-27 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcity', '0005_auto_20180227_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='pic',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
