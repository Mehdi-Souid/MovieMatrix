from django.db import models

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
    mov_year = models.PositiveIntegerField()
    mov_time = models.PositiveIntegerField(help_text="Durée en minutes")
    mov_lang = models.CharField(max_length=50)
    mov_dt_rel = models.DateField()
    mov_rel_country = models.CharField(max_length=5)
    genres = models.ManyToManyField(Genre, through='MovieGenre', related_name='movies')
    actors = models.ManyToManyField(Actor, through='MovieCast', related_name='movies')
    directors = models.ManyToManyField(Director, through='MovieDirection', related_name='movies')

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

class Reviewer(models.Model):
    rev_name = models.CharField(max_length=30)

    def __str__(self):
        return self.rev_name

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    rev_stars = models.PositiveSmallIntegerField()
    num_o_ratings = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.movie} rated {self.rev_stars} by {self.reviewer}"