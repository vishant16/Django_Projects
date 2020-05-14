from django import forms
from .models import signin

class UserForm(forms.ModelForm):

    class Meta:
        model = signin
        fields="__all__"
