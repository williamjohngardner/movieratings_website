from django.shortcuts import render
from movieratings.models import Movie, Rater, Rating


def index_page(request):
    movies = {"movies": list(Movie.objects.all())}
    return render(request, "index.html", movies)


def movie_page(request, movie_id):
    movies_dict = {"movies": list(Movie.objects.all()),
                   "raters": list(Rater.objects.all(user_id=movie_id)),
                   "ratings": list(Rating.objects.all())}

    return render(request, "movie_page.html", movies_dict)


def rater_page(request, rater):
    rater_dict = {"person": Rater.objects.filter(user_id=rater),
                  "ratings": Rating.objects.filter(user_id=rater),
                  "movies": Movie.objects.filter(movie_id=rater)}

    return render(request, "rater_page.html", rater_dict)

