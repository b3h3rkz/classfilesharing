# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 15:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Archive', '0005_upload_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='uploaded_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]