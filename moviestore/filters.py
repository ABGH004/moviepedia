from django_filters.rest_framework import FilterSet
from .models import Movie


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            "genre": ["exact"],
            "director": ["exact"],
            "actor": ["exact"],
            "rating": ["exact"],
            "score": ["lte", "gte"],
        }
