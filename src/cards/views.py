from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CardsRegisterForm

# Create your views here.


def cardregister(request):
    if request.method == 'POST':
        form = CardsRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your card has been added! ')
            return redirect('profile')
    else:
        form = CardsRegisterForm()
    return render(request, 'cards/cards_form.html', {'form': form})
