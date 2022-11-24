from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
@api_view(['GET', 'DELETE'])
def profile_detail(request, user_pk):
    User = get_user_model()
    person = get_object_or_404(User, pk=user_pk)
    if request.method == 'GET': 
        reviews = person.reviews.all()
        movies= person.score.all()
        review_json = []
        movie_json = []
        for review in reviews:
            review_movie = review.movie
            review_json.append(
            {
                'id': review.id,
                'title': review.title,
                'content': review.content,
                'movie_poster': review_movie.poster_path,
                'movie_id': review_movie.id,
                'movie_title': review_movie.title
            }
            )
        for movie in movies:
            movie_json.append(
            {
                'movie_id': movie.movie_id,
                'score' : movie.score 
            }
            )
        context = {
            'my_reviews' : review_json,
            'my_movies' : movie_json,
        }
        return JsonResponse(context)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)