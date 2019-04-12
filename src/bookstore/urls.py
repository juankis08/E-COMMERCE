from django.urls import path
from . import views
from .models import Book
#from books.models import Comment
from books import views as bookviews

urlpatterns = [
    path('', views.home, name='home_page'),
    path('about/', views.about, name='home_about'),
    path('wishlist/', views.wishlist, name='wish_list'),
    path('add-to-wishlist/<int:bookID>', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:bookID>', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('book/<int:pk>/comment/', bookviews.add_review_to_book, name='add_review_to_book'),
    path('comment/<int:pk>/approve/', bookviews.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', bookviews.comment_remove, name='comment_remove'),
]