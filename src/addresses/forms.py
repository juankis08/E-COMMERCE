from django import forms
from .models import Address
from django.contrib.auth.models import User

class AddressRegisterForm(forms.ModelForm):
    #class meta renders the the form as exactly is displayed in admin django web page
     
    class Meta:
        model = Address
        fields = ['address_type', 'address_line_1',
                  'address_line_2', 'city', 'state', 'zip_code', 'country']
