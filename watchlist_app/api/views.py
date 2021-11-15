# where the business logic happens with regards to the app

from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response

# import all the models here
from watchlist_app.models import WatchList, StreamPlatform

#import the serializers here
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer


# class based view

class StreamPlatform(APIView):
    
    #crud operations

    def get(self, request):
        stream_platforms = StreamPlatform.objects.all()
        serializer = WatchListSerializer(stream_platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

    def put(self, request, pk):
        stream_platform = StreamPlatform.objects.get(id=pk)
        serializer = StreamPlatformSerializer(instance=stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        stream_platform = StreamPlatform.objects.get(id=pk)
        stream_platform.delete()
        return Response('Deleted')



class StreamPlatformDetailView(APIView):
    
    # stream platform must be in the list
    def get(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(id=pk)
        except:
            raise StreamPlatform.DoesNotExist('Stream Platform  do not exit')

        serializer = StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)


class WatchListView(APIView):

    #crud operations
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer  = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class WatchListDetailView(APIView):
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error":"Movie Detail do not exit"}, status=404)
        
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            watchlist = WatchListSerializer.objects.get(pk=pk)
        except WatchListSerializer.DoesNotExist:
            return Response({'error': "No such item"}, status=404)

        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    
    def delete(self, pk):
        movie = WatchListSerializer.objects.get(pk=pk)
        movie.delete()
        return Response('Deleted')


# function based view to render the index page
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, id):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=id)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
        
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=id)
#         serializer = MovieSerializer(movie, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=id)
#         movie.delete()
#         return Response('Deleted')