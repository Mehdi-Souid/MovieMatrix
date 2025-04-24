from django.shortcuts import render
from .models import Movie
from django.shortcuts import render, redirect
from .models import Movie

def movie_list(request):
    # Récupère tous les films
    movies = Movie.objects.all()
    # Passe la liste au template
    return render(request, 'movies/movie_list.html', {'movies': movies})
