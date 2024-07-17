from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import  ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile



class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'mobile_number', 'age', 'profile_photo']
