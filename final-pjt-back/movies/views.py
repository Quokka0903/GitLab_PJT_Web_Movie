from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieScoreSerializer
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

@api_view(['POST', 'PUT'])
def CreateScore(request):
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
        


# 영화에 작성된 리뷰 목록 출력하기
