from django.shortcuts import render, redirect

from books.models import Book
from .models import Cart



def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    # total = 0 
    # for x in products:
    #     total += x.price
    # print(total)
    # cart_obj.total = total
    # cart_obj.save()
    return render(request, "carts/home.html", {"cart": cart_obj})
    

def cart_update(request):
    print(request)    
    product_id =  request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Book.objects.get(id=product_id) 
        except Book.DoesNotExist:
            print("show message to user, profuct is gone")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home")    