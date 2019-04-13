from django.urls import path
from django.urls import include
from .models import Book, Comment

from . import views

urlpatterns = [

    # path('', views.BookListView.as_view(), name="book_list"),
    # path('^(?P<pk>\d+)/$', views.BookDetailView.as_view(), name="book_detail"),
    path('', views.book_list_view, name="book_list"),
    path('details/<int:index>/',views.book_detail_view, name='book_detail'),
    path('refined-search/', views.refined_view, name="refined_view"),
    path('sorted/', views.sorted_book, name="sorted"),
    path('book/<int:pk>/comment/<str:anon>/', views.add_review_to_book, name='add_review_to_book'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('books/', views.book_list_view),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    

]

