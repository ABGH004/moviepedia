from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAdminUser
from .filters import MovieFilter
from .pagination import MoviePagination, GenreActorDirectorPagination
from .models import Movie, Genre, Director, Actor
from .serializers import (
    GetSimpleMovieSerializer,
    GetDetailedMovieSerializer,
    PostMovieSerializer,
    GenreSerializer,
    DirectorSerializer,
    ActorSerializer,
)

# Create your views here.


class MovieViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]

    queryset = Movie.objects.prefetch_related("genre", "director", "actor").all()

    serializer_classes = {
        "list": GetSimpleMovieSerializer,
        "retrieve": GetDetailedMovieSerializer,
        "create": PostMovieSerializer,
        "update": PostMovieSerializer,
    }
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = MovieFilter
    pagination_class = MoviePagination
    search_fields = ["title", "director__name", "actor__name", "genre__name"]
    ordering_fields = ["rating", "score", "release_date"]

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = GenreActorDirectorPagination

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = GenreActorDirectorPagination

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = GenreActorDirectorPagination

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]
