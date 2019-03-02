from django.shortcuts import render
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

def wishlist(request):
    wishlist = WishList.objects.all()

    context = {
        "test": wishlist,
        "wishlist": [
            {
                "title": "An Introduction to Science and Technology Studies 2nd Edition",
                "absolute_url": "google.com",
                "image": { "url": "https://3c1703fe8d.site.internapcdn.net/newman/gfx/news/hires/2017/whatisspacet.jpg" }
            },
            {
                "title": "An Introduction to Science and Technology Studies 2nd Edition",
                "absolute_url": "google.com",
                "image": { "url": "https://3c1703fe8d.site.internapcdn.net/newman/gfx/news/hires/2017/whatisspacet.jpg" }
            }
        ]
    }
    return render(request, 'bookstore/wishlist.html', context)