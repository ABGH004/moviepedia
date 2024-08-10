from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import validate_file_size


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    RATING_GENERAL = "G"
    RATING_PARENTAL_GUIDE = "PG"
    RATING_STRONG_CAUTION = "PG-13"
    RATING_RESTRICT = "R"
    RATING_ADULT = "NC-17"

    RATING_CHOICES = [
        (RATING_GENERAL, "G"),
        (RATING_PARENTAL_GUIDE, "PG"),
        (RATING_STRONG_CAUTION, "PG-13"),
        (RATING_RESTRICT, "R"),
        (RATING_ADULT, "NC-17"),
    ]

    title = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to="moviestore/images",
        blank=True,
        null=True,
        validators=[
            validate_file_size,
        ],
    )

    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)

    rating = models.CharField(
        max_length=5, choices=RATING_CHOICES, default=RATING_GENERAL
    )

    score = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )

    genre = models.ManyToManyField(Genre)

    # main actors(at most 5)
    actor = models.ManyToManyField(Actor)

    director = models.ManyToManyField(Director)

    def __str__(self) -> str:
        return self.title
