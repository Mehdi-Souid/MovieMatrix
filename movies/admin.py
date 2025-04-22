from django.contrib import admin
from .models import (
    Genre, Movie, Actor, Director, Reviewer,
    Rating, MovieCast, MovieDirection, MovieGenre
)

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Reviewer)
admin.site.register(Rating)
admin.site.register(MovieCast)
admin.site.register(MovieDirection)
admin.site.register(MovieGenre)
