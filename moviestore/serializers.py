from rest_framework import serializers
from .models import Movie, Genre, Director, Actor


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Genre
        fields = ["id", "name"]


class DirectorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Director
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Actor
        fields = ["id", "name"]


class GetSimpleMovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "rating",
            "genre",
            "score",
            "actor",
            "director",
            "release_date",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data["release_date"]:
            data["release_date"] = "Has'nt been released yet."
        return data


class GetDetailedMovieSerializer(serializers.ModelSerializer):

    genre = GenreSerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "image",
            "description",
            "rating",
            "genre",
            "score",
            "actor",
            "director",
            "release_date",
        ]


class PostMovieSerializer(serializers.ModelSerializer):
    MAX_ACTOR_CHOICE = 5
    MAX_DIRECTOR_CHOICE = 3
    MAX_GENRE_CHOICE = 3
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    director = serializers.PrimaryKeyRelatedField(
        queryset=Director.objects.all(), many=True
    )
    actor = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "image",
            "description",
            "rating",
            "genre",
            "score",
            "actor",
            "director",
            "release_date",
        ]

    def validate_genre(self, value):
        if not value:
            raise serializers.ValidationError("This field may not be blank.")
        elif len(value) > self.MAX_GENRE_CHOICE:
            raise serializers.ValidationError(
                f"You cannot specify more than {self.MAX_GENRE_CHOICE} genres. try only mentioning main genres of your chosen movie."
            )
        return value

    def validate_director(self, value):
        if not value:
            raise serializers.ValidationError("This field may not be blank.")
        elif len(value) > self.MAX_DIRECTOR_CHOICE:
            raise serializers.ValidationError(
                f"You cannot specify more than {self.MAX_DIRECTOR_CHOICE} directors. try only mentioning main directors of your chosen movie."
            )
        return value

    def validate_actor(self, value):
        if not value:
            raise serializers.ValidationError("This field may not be blank.")
        elif len(value) > self.MAX_ACTOR_CHOICE:
            raise serializers.ValidationError(
                f"You cannot specify more than {self.MAX_ACTOR_CHOICE} actors. try only mentioning main actors of your chosen movie."
            )
        return value
