from django.urls import path
from . import views, AlgoTest

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('score/', views.create_score),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('reviews/<int:review_pk>/likes/', views.likes),
    path('Algo/', AlgoTest.recommend),
]
