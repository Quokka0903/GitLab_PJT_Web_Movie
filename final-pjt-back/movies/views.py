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
        # articles = Article.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def CreateScore(request):
    print(1)
    serializer = MovieScoreSerializer(data=request.data)
    print(serializer)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        print(2)
        serializer.save(user=request.user)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

