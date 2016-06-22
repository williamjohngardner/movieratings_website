from django.db import models


class Movie(models.Model):
    movie_title = models.CharField(max_length=60)
    release_date = models.CharField(max_length=15)
    video_release_date = models.CharField(max_length=10, default="")
    IMDb_URL = models.URLField()
    unknown = models.IntegerField()
    action = models.IntegerField()
    adventure = models.IntegerField()
    animation = models.IntegerField()
    childrens = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    documentary = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    film_noir = models.IntegerField()
    horror = models.IntegerField()
    musical = models.IntegerField()
    mystery = models.IntegerField()
    romance = models.IntegerField()
    sci_fi = models.IntegerField()
    thriller = models.IntegerField()
    war = models.IntegerField()
    western = models.IntegerField()

    def __str__(self):
        return self.movie_title


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)

    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    user = models.ForeignKey(Rater)
    item = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return str(self.rating)


class AverageRating(models.Model):
    movie = models.ForeignKey(Movie)
    count_ratings = models.IntegerField()
    average_rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.movie)
