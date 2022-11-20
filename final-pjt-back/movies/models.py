from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    # 리뷰에 좋아요 누른 user 추가 
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# movies_liked 어떻게 할 지
class MovieScore(models.Model):
    # TODO: Float로 변경
    score = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="score")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="moviescore")

class Cinema(models.Model):
    pass