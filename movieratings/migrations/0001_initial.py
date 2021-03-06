# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=60)),
                ('release_date', models.CharField(max_length=15)),
                ('video_release_date', models.CharField(default='', max_length=10)),
                ('IMDb_URL', models.URLField()),
                ('unknown', models.IntegerField()),
                ('action', models.IntegerField()),
                ('adventure', models.IntegerField()),
                ('animation', models.IntegerField()),
                ('childrens', models.IntegerField()),
                ('comedy', models.IntegerField()),
                ('crime', models.IntegerField()),
                ('documentary', models.IntegerField()),
                ('drama', models.IntegerField()),
                ('fantasy', models.IntegerField()),
                ('film_noir', models.IntegerField()),
                ('horror', models.IntegerField()),
                ('musical', models.IntegerField()),
                ('mystery', models.IntegerField()),
                ('romance', models.IntegerField()),
                ('sci_fi', models.IntegerField()),
                ('thriller', models.IntegerField()),
                ('war', models.IntegerField()),
                ('western', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('occupation', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings.Rater')),
            ],
        ),
    ]
