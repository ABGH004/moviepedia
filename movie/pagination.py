from rest_framework.pagination import PageNumberPagination


class MoviePagination(PageNumberPagination):
    page_size = 5


class GenreActorDirectorPagination(PageNumberPagination):
    page_size = 20
