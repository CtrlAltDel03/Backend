from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email=forms.EmailFeild()

	class Meta:
		model=User
		fields=['username','email','passowrd1','passowrd2']
		
