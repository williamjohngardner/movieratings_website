from django.shortcuts import render
from movieratings.models import Movie, Rater, Rating


def index_page(request):
    movies = {"movies": list(Movie.objects.all())}
    return render(request, "index.html", movies)


def movie_page(request, movie):
    movies_dict = {"people": Rater.objects.filter(user_id=movie),
                   "ratings": Rating.objects.filter(user_id=movie),
                   "movies": Movie.objects.filter(movie_id=movie)}

    return render(request, "movie_page.html", movies_dict)


def rater_page(request, rater):
    rater_dict = {"person": Rater.objects.filter(user_id=rater),
                  "ratings": Rating.objects.filter(user_id=rater),
                  "movies": Movie.objects.filter(movie_id=rater)}

    return render(request, "rater_page.html", rater_dict)


def database(request):
    db_dict = {"movies": Movie.objects.all()}

    return render(request, "database_list.html", db_dict)


def twenty(request):
    pass

    return render(request, "twenty.html")

