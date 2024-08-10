from django.contrib import admin
from django.utils.html import format_html
from .models import Movie, Director, Actor, Genre


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ["moviestore/styles.css"]}

    autocomplete_fields = [
        "genre",
        "director",
        "actor",
    ]

    list_display = [
        "title",
        "thumbnail",
        "rating",
        "score",
        "genres",
        "directors",
        "actors",
        "release_date",
    ]

    list_editable = [
        "score",
    ]

    list_per_page = 10

    list_filter = [
        "genre",
    ]
    readonly_fields = ["thumbnail"]
    search_fields = ["title", "director__name", "actor__name"]

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(f'<img src="{instance.image.url}" class="thumbnail"/>')
        return ""

    def genres(self, obj):
        return ", ".join([g.name for g in obj.genre.all()])

    def directors(self, obj):
        return ", ".join([d.name for d in obj.director.all()])

    def actors(self, obj):
        return ", ".join([a.name for a in obj.actor.all()])


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]
    ordering = ["name"]


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]
