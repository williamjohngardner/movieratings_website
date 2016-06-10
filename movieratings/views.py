from django.shortcuts import render
from movieratings.models import Movie, Rater, Rating


def index_page(request):
    movies = {"movies": list(Movie.objects.all())}
    return render(request, "index.html", movies)


def top_twenty(request):
    pass


def new_rating(request):
    pass


def movie_page(request, movie_id):
    movies_dict = {"movies": list(Movie.objects.all()),
                   "raters": list(Rater.objects.all(user_id=movie_id)),
                   "ratings": list(Rating.objects.all())}

    return render(request, "movie_page.html", movies_dict)


def rater_page(request, rater_id):
    rater_dict = {"rater": list(Rater.objects.get(id=rater_id)),
                  "ratings": list(Rating.objects.filter(rater_id=rater_id)),
                  "movies": list(Movie.objects.all())}

    return render(request, "rater_page.html", rater_dict)

