from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# import all the models here
from watchlist_app.models import Movie

#import the serializers here
from watchlist_app.api.serializers import MovieSerializer

# function to render the index page
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
        
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializer(movie, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)