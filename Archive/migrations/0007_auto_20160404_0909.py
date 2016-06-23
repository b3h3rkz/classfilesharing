# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Archive', '0006_upload_uploaded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Archive.Level'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='upload',
            unique_together=set([('file', 'uploaded_by')]),
        ),
    ]
