# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-23 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chin_angle', models.FloatField()),
                ('mofa_ratio', models.FloatField()),
                ('hlmo_angle', models.FloatField()),
                ('shape', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='face',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faces', to='facerecog_app.User'),
        ),
    ]
