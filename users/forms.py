# Third party imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Local application import
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
        Creates User registration form for signing up.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
        Creates form for user to upadate their account.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
       Creates form for user to update their Profile.
    """
    class Meta:
        model = Profile
        fields = ['image']
