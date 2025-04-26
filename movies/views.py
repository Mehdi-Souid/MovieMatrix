from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm
)
from django.db.models import Avg, Q
from .forms import CustomUserCreationForm
from .models import Movie, Wishlist, Genre, Rating
from .forms import RatingForm

def home(request):
    genre_filter = request.GET.get('genre')
    sort_by = request.GET.get('sort')
    search_query = request.GET.get('search')

    movies = Movie.objects.annotate(avg_rating=Avg('ratings__rev_stars'))

    if genre_filter:
        movies = movies.filter(genres__id=genre_filter)

    if search_query:
        movies = movies.filter(
            Q(mov_title__icontains=search_query) |
            Q(mov_lang__icontains=search_query) |
            Q(mov_rel_country__icontains=search_query)
        )

    if sort_by == 'rating':
        movies = movies.order_by('-avg_rating')
    elif sort_by == 'newest':
        movies = movies.order_by('-mov_dt_rel')
    else:
        movies = movies.order_by('-mov_year')

    genres = Genre.objects.all()
    
    return render(request, 'movies/home.html', {
        'movies': movies,
        'genres': genres,
        'current_genre': int(genre_filter) if genre_filter else '',
        'current_sort': sort_by,
        'search_query': search_query or ''
    })
    
def movie_detail(request, movie_id):
    movie = get_object_or_404(
        Movie.objects.annotate(avg_rating=Avg('ratings__rev_stars'))
        .prefetch_related('moviecast_set__actor', 'moviedirection_set__director'),
        pk=movie_id
    )
    
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(movie=movie, user=request.user).first()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")
            
        form = RatingForm(request.POST)
        if form.is_valid():
            if user_rating:
                user_rating.rev_stars = form.cleaned_data['rev_stars']
                user_rating.save()
            else:
                Rating.objects.create(
                    movie=movie,
                    user=request.user,
                    rev_stars=form.cleaned_data['rev_stars']
                )
            messages.success(request, "Rating saved!")
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = RatingForm(instance=user_rating)

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'form': form,
        'user_rating': user_rating,
        'existing_rating': user_rating.rev_stars if user_rating else None
    })

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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can now login.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.title()}: {error}")
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def wishlist(request):
    search_query = request.GET.get('search')
    genre_filter = request.GET.get('genre')
    sort_by = request.GET.get('sort')

    wishlist_items = Wishlist.objects.filter(user=request.user) \
        .select_related('movie') \
        .annotate(avg_rating=Avg('movie__ratings__rev_stars'))

    if search_query:
        wishlist_items = wishlist_items.filter(
            Q(movie__mov_title__icontains=search_query) |
            Q(movie__mov_lang__icontains=search_query) |
            Q(movie__mov_rel_country__icontains=search_query)
        )

    if genre_filter:
        wishlist_items = wishlist_items.filter(movie__genres__id=genre_filter)

    if sort_by == 'rating':
        wishlist_items = wishlist_items.order_by('-movie__avg_rating')
    elif sort_by == 'newest':
        wishlist_items = wishlist_items.order_by('-movie__mov_dt_rel')
    else:
        wishlist_items = wishlist_items.order_by('-movie__mov_year')

    genres = Genre.objects.all()
    
    return render(request, 'movies/wishlist.html', {
        'wishlist_items': wishlist_items,
        'genres': genres,
        'current_genre': int(genre_filter) if genre_filter else '',
        'current_sort': sort_by,
        'search_query': search_query or ''
    })
    
@login_required
def remove_from_wishlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    Wishlist.objects.filter(user=request.user, movie=movie).delete()
    return redirect('wishlist')
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Password updated successfully!')
            return redirect('edit_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'registration/edit_profile.html', {
        'form': form
    })