# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 19:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiments', '0008_auto_20180503_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]