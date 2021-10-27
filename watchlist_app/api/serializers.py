
from rest_framework import serializers

# import movie models
from watchlist_app.models import Movie

#movie serializers
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    description = serializers.CharField(required=True, allow_blank=False, max_length=500)
    IsActive = serializers.BooleanField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    # cretes a new movie
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.IsActive = validated_data.get('IsActive', instance.IsActive)
        instance.save()
        return instance
