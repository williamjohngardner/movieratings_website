from django.shortcuts import render
from movieratings.models import Movie, Rater, Rating


def index_page(request):
    movies = {"movies": list(Movie.objects.all())}
    return render(request, "index.html", movies)


def top_twenty(request):
    pass


def new_rating(request):
    pass


def movie_page(request):
    movies = {"movies": list(Movie.objects.all())}
    return render(request, "movie_page.html", movies)


def rater_page(request):
    raters = {"raters": list(Rater.objects.all())}
    return render(request, "rater_page.html", raters)
