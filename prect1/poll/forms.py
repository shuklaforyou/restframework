from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Poll




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2']



class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['user','question', 'option_one', 'option_two', 'option_three']

        widgets={
            'user':forms.HiddenInput()
        }