from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile,NewsAndUpdates


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Email Address'}))
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Username'}))
    password1 = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', required=True, max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = '__all__'

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Username'}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Password'}))

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class NewsUploads(forms.ModelForm):
    class Meta:
        model = NewsAndUpdates
        fields = ('title','doc')