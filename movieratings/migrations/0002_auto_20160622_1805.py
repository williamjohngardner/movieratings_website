# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 20:03
from __future__ import unicode_literals
from django.db import migrations
import csv


def movie_data(apps, schema_editor):
    Movie = apps.get_model("movieratings", "Movie")

    with open("u.item", encoding="latin1") as infile:
        csv_item = csv.reader(infile, delimiter='|')

        for row in csv_item:
            Movie.objects.create(id=row[0], movie_title=row[1], release_date=row[2], video_release_date=row[3],
                                 IMDb_URL=row[4], unknown=row[5], action=row[6], adventure=row[7], animation=row[8],
                                 childrens=row[9], comedy=row[10], crime=row[11], documentary=row[12], drama=row[13],
                                 fantasy=row[14], film_noir=row[15], horror=row[16], musical=row[17], mystery=row[18],
                                 romance=row[19], sci_fi=row[20], thriller=row[21], war=row[22], western=row[23])

    # raise Exception("Movie yay!")


def rater_data(apps, schema_editor):
    Rater = apps.get_model("movieratings", "Rater")

    with open("u.user") as infile:
        csv_item = csv.reader(infile, delimiter='|')

        for row in csv_item:
            Rater.objects.create(id=row[0], age=row[1], gender=row[2], occupation=row[3], zip_code=row[4])

    # raise Exception("Rater yay!")


def rating_data(apps, schema_editor):
    Rating = apps.get_model("movieratings", "Rating")
    Movie = apps.get_model("movieratings", "Movie")
    Rater = apps.get_model("movieratings", "Rater")

    with open("u.data") as infile:
        csv_item = csv.reader(infile, delimiter='\t')

        for row in csv_item:
            movie = Movie.objects.get(id=row[1])
            rater = Rater.objects.get(id=row[0])

            Rating.objects.create(user=rater, item=movie, rating=row[2], timestamp=row[3])

    # raise Exception("Rating yay!")


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(movie_data),
        migrations.RunPython(rater_data),
        migrations.RunPython(rating_data)
    ]