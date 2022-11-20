from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieScoreSerializer, ReviewListSerializer, ReviewSerializer, MovieSerializer, GenreSerializer
from .models import Movie, Genre, Review, MovieScore
from django.http import JsonResponse
import requests
import json
import random

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        # movies = Movie.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

# TODO: movie detail 페이지로, 좋아요 상위 5개만 보내는 함수 만들기
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

# 영화에 대한 평점
@api_view(['POST'])
def create_score(request):
    if request.method == 'POST':
        movie_pk = request.data['movie_pk']
        movies = MovieScore.objects.all()
        newdata = {
            'score': request.data['score'],
        }
        for movie in movies:
            print(movie)
            if movie.movie_id == movie_pk and movie.user_id == request.user.pk:
                deleted_id = movie.id
                tmp_movie = get_object_or_404(MovieScore, pk=deleted_id)
                serializer = MovieScoreSerializer(tmp_movie, data=newdata)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
                # tmp_movie.delete()
                # break
        else:
            newmovie = get_object_or_404(Movie, pk=movie_pk)
            serializer = MovieScoreSerializer(data=newdata)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie=newmovie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 수정 어떻게 할 지
    # elif request.method == 'PUT':

# def movie_detail(request):
# @api_view(['GET'])
# def review_list(request):
#     if request.method == 'GET':
#         reviews = get_list_or_404(Review)
#         serializer = ReviewListSerializer(reviews, many=True)
#         return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    # 리뷰는 각 component로 가져올 것 이므로 GET 필요
    review = get_object_or_404(Review, pk=review_pk)
    # 불러오기
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    # 삭제하기
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 수정하기
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 리뷰 작성하기
@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 좋아요 구현
@api_view(['POST'])
def likes(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True    
    like_count = review.like_users.count()
    context = {
        'like_count': like_count,
        'is_liked': is_liked,
        'pk': review_pk,
    }
    return JsonResponse(context)

@api_view(['GET'])
def recommend_genre(request, movie_id):
    # 장르가 같은 모든 영화 가져오기
    movie = get_object_or_404(Movie, pk=movie_id)
    genres = movie.genres.all()
    movie_list = []
    if len(genres) == 1:
        for genre in genres:
            movies = genre.movie_set.all()
            movie_list.append(random.sample(list(movies), 10))
            for mo in random.sample(list(movies), 5):
                movie_list.append(mo)
    else:
        for genre in genres:
            movies = genre.movie_set.all()
            for mo in random.sample(list(movies), 5):
                movie_list.append(mo)
    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)