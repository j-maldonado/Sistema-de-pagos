from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class Login_User(ModelForm):
    pass

class RegisterUser(UserCreationForm):
    password1= forms.CharField(
        label='Password', 
        strip=False, 
        widget=forms.PasswordInput, 
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2= forms.CharField(
        label='Repetir Password', 
        strip=False, 
        widget=forms.PasswordInput, 
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model=User
        labels={'username':'Nombre de Usuario', 
        'email': 'Email',
        }
        fields=['username', 'email']



