from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField()
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
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)

    def __str__(self):
        return str(self.user_id)


class Rating(models.Model):
    user_id = models.IntegerField()
    item_id = models.IntegerField()
    rating = models.IntegerField()
    timestamp = models.IntegerField()
    movie_id = models.ForeignKey(Movie)
    rater_id = models.ForeignKey(Rater)

    def __str__(self):
        return str(self.rating)