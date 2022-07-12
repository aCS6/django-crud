from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.Home.as_view() , name="home"),
    path("upload/", views.upload , name="upload"),
    path("movies/", views.movie_list , name="movie_list"),
    path("movies/upload/", views.add_movie , name="add_movie"),
    path("movies/delete/<int:pk>", views.delete_movie, name="delete_movie"),
    path("movies/update/<int:pk>", views.update_movie, name="update_movie")
]
