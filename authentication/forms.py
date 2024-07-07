from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 7  # Set max length for username field

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        labels = {
            'password': 'Password',
            'password2': 'Confirm Password',
        }
        widgets = {
            'password': forms.PasswordInput(render_value=True),
            'password2': forms.PasswordInput(render_value=True),
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
