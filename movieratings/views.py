from django.shortcuts import render, redirect
from movieratings.models import Movie, Rater, Rating, AverageRating
from movieratings.forms import RatingForm


def index_page(request):
    movies = {"movies": list(Movie.objects.all())}
    return render(request, "index.html", movies)


def movie_page(request, movie):
    movies_dict = {
                   "ratings": Rating.objects.filter(item__id=movie),
                    "movies": Movie.objects.filter(id=movie)
                }

    return render(request, "movie_page.html", movies_dict)


def rater_page(request, rater):
    rater_dict = {"person": Rater.objects.filter(id=rater),
                  "ratings": Rating.objects.filter(user_id=rater),
                  "movies": Movie.objects.filter(id=rater)}

    return render(request, "rater_page.html", rater_dict)


def database(request):
    db_dict = {
                "movies": Movie.objects.all()
              }

    return render(request, "database_list.html", db_dict)


def twenty(request):
    context = {
        "top_20": AverageRating.objects.filter(count_ratings__gt=100).order_by("-average_rating")[:20],
    }
    return render(request, 'twenty.html', context)


def new_rating(request, movie_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = Rater.objects.get(id=944)
            post.item_id = Movie.objects.get(id=movie_id)
            post.rating = form.cleaned_data['rating']
            post.save()
            return redirect('movieratings.views.movie_view', movie_id=movie_id)
    else:
        form = RatingForm()

    context = {
        "movie": Movie.objects.get(id=movie_id),
        "form": form
    }
    return render(request, 'new_rating.html', context)