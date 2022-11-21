from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('score/', views.create_score),
    path('score/<int:movie_pk>/<int:user_pk>', views.score_view),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('reviews/<int:review_pk>/likes/', views.likes),
    path('algo/', views.recommend),
    path('genre_algo/<int:movie_id>/', views.recommend_genre),
    path('like/', views.like_movies),
    path('genre/', views.random_genre),
    path('movies/reviews/<int:movie_id>/', views.review_list),
]
