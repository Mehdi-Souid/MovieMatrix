from django.contrib import admin
from .models import (
    Genre,
    Actor,
    Director,
    Movie,
    MovieGenre,
    MovieCast,
    MovieDirection,
    Rating,
    Wishlist  
)

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(MovieGenre)
admin.site.register(MovieCast)
admin.site.register(MovieDirection)
admin.site.register(Rating)
admin.site.register(Wishlist)  