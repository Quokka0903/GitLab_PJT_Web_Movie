from rest_framework import serializers
from .models import Movie, MovieScore


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieScoreSerializer(serializers.ModelSerializer):
        class Meta:
            model = MovieScore
            fields = '__all__'
            read_only_fields = ('user', 'movie' )
