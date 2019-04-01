from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('about/', views.about, name='home_about'),
    path('wishlist/', views.wishlist, name='wish_list'),
    path('create-wishlist/<int:userID>/<int:wishlistID>/<str:name>', views.create_wistlist, name='create_wishlist'),
    path('delete-wishlist/<int:userID>/<int:wishlistID>', views.delete_wistlist, name='create_wishlist'),
    path('add-to-wishlist/<int:bookID>', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:bookID>', views.remove_from_wishlist, name='remove_from_wishlist')
]