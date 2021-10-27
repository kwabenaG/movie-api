from django.urls import path

#views Class
from .views import MovieListView, MovieDetailView

# views functions
# from .views import movie_list, movie_detail

urlpatterns = [

    #class base url
    path('', MovieListView.as_view()),
    path('<int:pk>/', MovieDetailView.as_view()),


    #func based url
    # path('', movie_list , name='movie_list'),
    # path('<int:id>/', movie_detail, name='movie_detail'),
]

