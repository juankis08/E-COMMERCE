from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('about/', views.about, name='home_about'),
    path('wishlist/', views.wishlist, name='wish_list')
]