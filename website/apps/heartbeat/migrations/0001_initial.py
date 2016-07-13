# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-13 16:18
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
            name='Beat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='beat', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated',),
                'verbose_name': 'Beat',
            },
        ),
    ]
