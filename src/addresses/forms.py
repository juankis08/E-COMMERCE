from django import forms
from .models import Address

class AdressForm(forms.ModelForm):
    #class meta renders the the form as exactly is displayed in admin django web page
    class Meta:
        model = Address