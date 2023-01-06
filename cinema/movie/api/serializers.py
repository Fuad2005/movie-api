from rest_framework import serializers
from ..models import Movie, Review
from django.db.models import Avg



class ReviewSerializer(serializers.ModelSerializer):
    movie_name = serializers.StringRelatedField(source="movie")
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # reviews = serializers.StringRelatedField(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True)
    reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')
    average_star = serializers.SerializerMethodField()


    def validate_imdb(self, value):
        if not 0 <= value <= 10:
            raise serializers.ValidationError('imbd must be between 0 and 10')
        return value



    def get_average_star(self, obj):
        return obj.reviews.aggregate(avg=Avg('stars')).get('avg')

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1
