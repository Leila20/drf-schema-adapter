# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-04-27 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_product_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='howitworks',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
