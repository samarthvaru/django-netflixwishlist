from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']




class ListForm(ModelForm):
    class Meta:
        model = ListItem
        fields = '__all__'
        exclude = []
        widgets={'customer':forms.HiddenInput()}


class UpdateForm(ModelForm):
    class Meta:
        model=ListItem
        fields='__all__'
        exclude=['customer']




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model=Customer
        fields=['name']
