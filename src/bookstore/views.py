from django.shortcuts import render, redirect
from books.models import Book,Author
from accounts.models import WishList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    books = Book.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(books, 12)
    try:
        book_by_page = paginator.page(page)
    except PageNotAnInteger:
        book_by_page = paginator.page(1)
    except EmptyPage:
        book_by_page = paginator.page(paginator.num_pages)

    context = {'book_by_page': book_by_page}
    return render(request, 'bookstore/home.html', context)
# Create your views here.

def about(request):
    return render(request, 'bookstore/about.html')

def add_to_wishlist(request, bookID):
    if WishList.objects.filter(user=request.user, book=Book.objects.get(id=bookID)).exists():
        return redirect('wish_list')
    wishlistItem = WishList(user=request.user, book=Book.objects.get(id=bookID))
    wishlistItem.save()
    return redirect('wish_list')

def remove_from_wishlist(request, bookID):
    WishList.objects.filter(user=request.user, book=Book.objects.get(id=bookID)).delete()
    return redirect('wish_list')

def wishlist(request):
    wishlist = WishList.objects.filter(user=request.user)
    context = {
        "wishlist": wishlist
    }
    return render(request, 'bookstore/wishlist.html', context)
