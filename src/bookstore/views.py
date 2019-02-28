from django.shortcuts import render
from books.models import Book,Author
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