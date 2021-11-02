from django.urls import path

#views Class
from .views import WatchListView, WatchListDetailView, StreamPlatform, StreamPlatformDetailView
# views functions
# from .views import movie_list, movie_detail

urlpatterns = [

    #class base url
    path('', WatchListView.as_view()),
    path('<int:pk>/', WatchListDetailView.as_view()),

    # stream platform url
    path('stream-platform-list', StreamPlatform.as_view(), name='stream_platform'),
    path('stream-platform-list/<int:pk>/', StreamPlatformDetailView.as_view(), name='stream_platform_list'),

    #func based url
    # path('', movie_list , name='movie_list'),
    # path('<int:id>/', movie_detail, name='movie_detail'),
]

