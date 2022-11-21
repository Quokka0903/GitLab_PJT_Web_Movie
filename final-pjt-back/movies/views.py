from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework import generics

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieScoreSerializer, ReviewListSerializer, ReviewSerializer, MovieSerializer, GenreSerializer
from .models import Movie, Genre, Review, MovieScore
from django.http import JsonResponse
from collections import defaultdict
import random
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
    
@api_view(['GET'])
def review_list(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        reviews = movie.review_set.all()
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

# 알고리즘 구현
@api_view(['GET'])
def recommend(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movie_scores = get_list_or_404(MovieScore, user_id=request.user.id)

        prefer = defaultdict(int)
        already_like = []
        for score in movie_scores:
            already_like.append(score.movie_id)
            movie = get_object_or_404(Movie, pk=score.movie_id)
            #print('movie')
            #print(movie.title)
            for genre in movie.genres.all():
                #print(genre.name, end=' ')
                prefer[genre.id] += 1
            #print('\n')

        movie_list = []

        #print('장르 점수')
        #print(prefer)
        #print('\n')

        for movie in movies:

            if movie.pk in already_like:
                 continue
            score = movie.vote_average * 3
            score += movie.popularity ** 0.5

            for genre in movie.genres.all():
                score += prefer[genre.id] * 3   
            movie_list.append([score, movie.id, movie.title])

        movie_list.sort(reverse=True)

        my_movies = movie_list[:15]
        my_movie = []
        for s, i, t in  movie_list[:15]:
            my_movie.append(movies[i - 1])

        # for unit in my_movies:
        #     print(unit[0], unit[2])

        #print(my_movie)

        serializer = MovieListSerializer(my_movie, many=True)
        return Response(serializer.data)
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

# 처음 영화 선택, 장르별로 중복없이 영화 가져오기
@api_view(['GET'])
def like_movies(request):
    movie_list = []
    genres = get_list_or_404(Genre)
    for genre in genres:
        movies = genre.movie_set.all().order_by('popularity')
        n = 0
        for movie in movies:
            if n == 5 or n == len(movies): 
                break
            if movie not in movie_list:
                movie_list.append(movie)
                n += 1
    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)

# main page에 들어갈 랜덤 장르
@api_view(['GET'])
def random_genre(request):
    genre = random.choice(get_list_or_404(Genre))
    movies = random.sample(list(genre.movie_set.all()), 4)
    serializer = MovieListSerializer(movies, many=True)
    context = {
        'genre': genre.name,
        'movies': serializer.data
    }
    
    # result = json.dumps(context, indent=4)
    # print(result)
    return Response(context) 

@api_view(['GET'])
def score_view(request, movie_pk, user_pk):
    try:
        movie_score = MovieScore.objects.get(movie=movie_pk, user=user_pk)
        serializer = MovieScoreSerializer(movie_score)
        return Response(serializer.data)
    except:
        return

# 검색기능 구현
class search_list(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']