# MovieMatrix: Movie Catalogue & Ratings

A Django web application to browse movies, see their cast and directors, rate them and keep a personal wishlist. Built as a school project.

## Features

- **Movie catalogue:** title, year, duration, language, release date and country, with poster images
- **Relational data model:** movies linked to genres, actors (with their role) and directors through many-to-many tables
- **Ratings:** logged-in users rate movies from 1 to 5 stars, with timestamps
- **Wishlist:** add or remove movies. Duplicates are prevented by a unique constraint
- **Accounts:** registration, login/logout (Django auth) and profile editing
- **Admin:** manage all data through the Django admin site

## Tech Stack

Python · Django 5.2 · SQLite · Django templates · HTML / CSS / JavaScript

## Data Model

```
Movie ──< MovieGenre >── Genre
Movie ──< MovieCast >── Actor        (role)
Movie ──< MovieDirection >── Director
Movie ──< Rating >── User            (1–5 stars)
Movie ──< Wishlist >── User          (unique per user)
```

## Getting Started

```bash
python -m venv venv
venv\Scripts\activate          # macOS/Linux: source venv/bin/activate
pip install django pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver     # http://127.0.0.1:8000
```

## Main Routes

| Route | Page |
|---|---|
| `/` | Home with the movie list |
| `/movie/<id>/` | Movie details, cast, rating |
| `/wishlist/` | Your wishlist |
| `/accounts/login/`, `/accounts/register/` | Authentication |
| `/profile/edit/` | Edit profile |
