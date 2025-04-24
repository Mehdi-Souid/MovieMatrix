from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Wishlist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'movies/wishlist.html', {'wishlist': wishlist_items})

@login_required
def add_to_wishlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    Wishlist.objects.get_or_create(user=request.user, movie=movie)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})