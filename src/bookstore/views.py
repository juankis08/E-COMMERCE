from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from books.models import Book,Author
from accounts.models import WishList, WishListNames
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


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

def create_wistlist(request, userID, wishlistID, name):
    user = User.objects.get(id=userID)
    WishListNames(user=user, wishlist_num=wishlistID, name=name).save()
    return JsonResponse({'msg':'Success'})

def delete_wistlist(request, userID, wishlistID):
    user = User.objects.get(id=userID)
    WishListNames.objects.get(user=user, wishlist_num=wishlistID).delete()
    return JsonResponse({'msg':'Success'})

def add_to_wishlist(request, wishlistID, bookID):
    if WishList.objects.filter(user=request.user, book=Book.objects.get(id=bookID)).exists():
        return JsonResponse({'msg':'Already exists'})
    wishlistItem = WishList(user=request.user, book=Book.objects.get(id=bookID), wishlist_num=wishlistID)
    wishlistItem.save()
    return JsonResponse({'msg':'Success'})

def remove_from_wishlist(request, bookID):
    WishList.objects.filter(user=request.user, book=Book.objects.get(id=bookID)).delete()
    return redirect('wish_list')

def wishlist(request):
    wishlist_names = WishListNames.objects.all()
    wishlist = WishList.objects.filter(user=request.user)
    wishlist_dict = {}
    wishlist_names_d = [None, None, None]
    for w in wishlist_names:
        wishlist_names_d[w.wishlist_num] = w

    context = {
        "wishlist": wishlist_dict,
        "wishlistNames": wishlist_names_d,
        "numWishlist": range(3),
    }

    return render(request, 'bookstore/wishlist.html', context)
