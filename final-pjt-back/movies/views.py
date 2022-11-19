from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieScoreSerializer, ReviewListSerializer, ReviewSerializer, MovieSerializer
from .models import Movie, Genre, Review

import requests
import json

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        # movies = Movie.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST', 'PUT'])
def create_score(request):
    if request.method == 'POST':
        movie_pk = request.data['movie_pk']
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        newdata = {
            'score': request.data['score'],
        }
        serializer = MovieScoreSerializer(data=newdata)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 수정 어떻게 할 지
    # elif request.method == 'PUT':

# TODO: movie detail 페이지로, 좋아요 상위 5개만 보내는 함수 만들기
# def movie_detail(request):
@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


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
        # TODO: data 체크하기
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
