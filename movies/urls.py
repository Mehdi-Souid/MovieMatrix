from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:movie_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:movie_id>/', 
     views.remove_from_wishlist, 
     name='remove_from_wishlist'),
    # Authentication URLs
     path('accounts/login/', 
         auth_views.LoginView.as_view(
             template_name='registration/login.html',
             redirect_authenticated_user=True
         ), 
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

]