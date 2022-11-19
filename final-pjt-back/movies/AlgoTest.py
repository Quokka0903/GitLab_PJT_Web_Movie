from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_safe, require_POST
from .serializers import MovieListSerializer
from .models import Movie, Genre, MovieScore

from collections import defaultdict

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


# @require_safe
def recommend(request):
    movies = get_list_or_404(Movie)
    movie_scores = get_list_or_404(MovieScore)

    prefer = defaultdict(int)
    already_like = []
    for score in movie_scores:
        if score.user_id == request.user.id:
            already_like.append(score.movie_id)
            movie = get_object_or_404(Movie, pk=score.movie_id)
            print('movie')
            print(movie.title)
            for genre in movie.genres.all():
                print(genre.name, end=' ')
                prefer[genre.id] += 1
            print('\n')
    
    movie_list = []
    
    print('장르 점수')
    print(prefer)
    print('\n')

    for movie in movies:
        
        if movie.pk in already_like:
             continue
        score = movie.vote_average * 3
        score += movie.popularity // 100
        
        for genre in movie.genres.all():
            score += prefer[genre.id] * 5
        movie_list.append([score, movie.pk, movie.title])
    
    movie_list.sort(reverse=True)

    my_movies = movie_list[:10]
    my_movie = []
    for s, i, t in  movie_list[:10]:
        my_movie.append(i)
    
    for unit in my_movies:
        print(unit[0], unit[2])

    context = {
        'my_movie' : my_movie,
        'movies' : movies,
    }
    
    # print(context)

    return 0
