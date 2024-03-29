from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

# Registration form
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-field-class'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-field-class'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-field-class'}),
        }

# Login form
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
