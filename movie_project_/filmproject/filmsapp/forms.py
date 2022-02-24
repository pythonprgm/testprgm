from django import forms
from .models import film

class Movieform(forms.ModelForm):
    class Meta:
        model=film
        fields=['name','desc','year','img']