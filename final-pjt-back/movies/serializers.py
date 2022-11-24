from rest_framework import serializers
from .models import Movie, MovieScore, Review, Genre


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path')

class MovieScoreSerializer(serializers.ModelSerializer):
    # user 처리 필요
    # username = serializers.CharField(source='user.username', read_only=True) 
    # movie = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = MovieScore
        fields = '__all__'
        read_only_fields = ('user', 'movie')


class ReviewListSerializer(serializers.ModelSerializer):
    # user 처리 필요
    # movie 처리 필요? (상관 없는 것 같기도)
    class Meta:
        model = Review
        fields = ('id',)
        read_only_fields = ('user', 'movie', 'like_users',)

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'like_users')

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# 단일 영화 Serializer
class MovieSerializer(serializers.ModelSerializer):
    # review_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    genres = GenreListSerializer(many=True, read_only=True)
    # user 처리 필요
    class Meta:
        model = Movie
        fields = '__all__'
