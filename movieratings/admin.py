from django.contrib import admin
from movieratings.models import Rating
from movieratings.models import Rater
from movieratings.models import Movie

admin.site.register([Rater, Rating, Movie])
