from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# from .forms import CreateUserForm 
from django.contrib.auth.models import User

def login_view(request):

		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				print('sukses')
				return redirect('homepage')
			else:
				print('gagal')

		context = {}
		return render(request, "login.html", context)


def register(request):
		if request.method == "POST":
			email = request.POST['email'] 
			username = request.POST['username'] 
			password = request.POST['password']
			password1 = request.POST['password1']
			if password != password1:
				print('password doesnt match')
				return render(request, 'register.html', {'message':'password doesnt match'})
			else:
				user = User.objects.create_user(username, email, password)
				return redirect('login')
		return render(request, "register.html")

def logout_view(request):
    logout(request)