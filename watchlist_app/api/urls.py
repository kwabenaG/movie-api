from django.urls import path

#views Class
from .views import WatchListView, WatchListDetailView, WatchListCreateView, WatchListUpdateView, WatchListDeleteView
# views functions
# from .views import movie_list, movie_detail

urlpatterns = [

    #class base url
    path('', WatchListView.as_view()),
    path('<int:pk>/', WatchListDetailView.as_view()),


    #func based url
    # path('', movie_list , name='movie_list'),
    # path('<int:id>/', movie_detail, name='movie_detail'),
]

