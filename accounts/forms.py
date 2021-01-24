from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Restorant
from django.forms import ModelForm

class CreateUserForm(UserCreationForm, forms.ModelForm):
	password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type' : 'password' }))
	password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type' : 'password' }))

	class Meta:
		model = User 
		fields = [
			'username', 'email', 'password1', 'password2' 

		]

		widgets = {
			'username' : forms.TextInput(attrs = {'class': 'form-control', }),
			'email' : forms.EmailInput(attrs = {'class': 'form-control', }),

		}

class Restoform(ModelForm):
	class Meta :
		model = Restorant
		fields = [
			'foto_resto', 'foto_menu', 'nama_resto', 'notlp', 'alamat',
		]

class UbahStatus(ModelForm):
	class Meta:
		model = Restorant
		fields = [
			'status'
		]
		





		
