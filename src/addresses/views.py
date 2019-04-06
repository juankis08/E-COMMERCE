from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddressRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Address

# Create your views here.


@login_required
def addressregister(request):
    Address.objects.all()
    #if request.method == 'POST':
    form = AddressRegisterForm(request.POST or None )
    if form.is_valid():
        fs=form.save(commit = False)
        fs.user = request.user
        fs.save()
        messages.success(
            request, f'Your address has been created! ')
        return redirect('address-home')
    else:
        form = AddressRegisterForm()
    return render(request, 'addresses/address_form.html', {'form': form})
