from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    gen_title = models.CharField(max_length=100)

    def __str__(self):
        return self.gen_title

class Actor(models.Model):
    act_fname = models.CharField(max_length=20)
    act_lname = models.CharField(max_length=20)
    act_gender = models.CharField(max_length=1, choices=[('M','Male'),('F','Female')])

    def __str__(self):
        return f"{self.act_fname} {self.act_lname}"

class Director(models.Model):
    dir_fname = models.CharField(max_length=20)
    dir_lname = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.dir_fname} {self.dir_lname}"

class Movie(models.Model):
    mov_title = models.CharField(max_length=200)
    mov_year = models.PositiveIntegerField(validators=[MinValueValidator(1888)])
    mov_time = models.PositiveIntegerField(help_text="Duration in minutes")
    mov_lang = models.CharField(max_length=50)
    mov_dt_rel = models.DateField()
    mov_rel_country = models.CharField(max_length=5)
    genres = models.ManyToManyField(Genre, through='MovieGenre', related_name='genres_movies')
    actors = models.ManyToManyField(Actor, through='MovieCast', related_name='actors_movies')
    directors = models.ManyToManyField(Director, through='MovieDirection', related_name='directors_movies')
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)

    def __str__(self):
        return self.mov_title

class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} - {self.genre}"

class MovieCast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.actor} as {self.role} in {self.movie}"

class MovieDirection(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.director} directs {self.movie}"

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Changed from Reviewer to User
    rev_stars = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Added timestamp

    def __str__(self):
        return f"{self.movie} rated {self.rev_stars} by {self.user.username}"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')  # Prevents duplicate entries

    def __str__(self):
        return f"{self.user.username}'s wishlist: {self.movie.mov_title}"