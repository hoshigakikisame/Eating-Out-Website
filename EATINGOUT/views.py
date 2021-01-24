from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from accounts.models import Restorant, Menu
from accounts.forms import Restoform, UbahStatus
from django.contrib.auth.models import User
from .forms import MenuForm

def index(request): 
	if request.user.is_authenticated:
		return redirect('homepage')
	return render(request, "index.html")

def homepage(request):
	all_resto = Restorant.objects.all()
	context = { 'all_resto':all_resto }
	if Restorant.objects.filter(milik=request.user).exists():
		context['resto_user'] = Restorant.objects.filter(milik=request.user).exists()
	return render(request, "homepage.html", context)

def resto(request, milik):
		
	resto_user = Restorant.objects.get(milik=milik)
	menu_resto = Menu.objects.filter(penyedia=resto_user)
	context = {
		'resto_user':resto_user,
		'menu_resto':menu_resto,
	}
	return render(request, "resto.html", context)

def rubah_menu(request, id_menu):
	menu = Menu.objects.get(id=id_menu)
	if menu.status == "Tersedia":
		menu.status = "Habis"
		menu.save()
	else:
		menu.status = "Tersedia"
		menu.save()
	return redirect('resto', milik=request.user.id)

def resto_status(request, id_resto):
	resto = Restorant.objects.get(id=id_resto)
	if resto.status == "Buka":
		resto.status = "Tutup"
		resto.save()
	else:
		resto.status = "Buka"
		resto.save()
	return redirect('resto', milik=request.user.id)

def daftarresto(request):
	form = Restoform(request.POST or None, request.FILES or None)

	context = {
		'form' : form,
	}

	if request.method == 'POST':
		if form.is_valid():
			data = form.save(commit=False)
			data.milik = User.objects.get(username=request.user)
			data.status = "Buka"
			data.save()
			return redirect('resto', milik=request.user.id)
		else:
			print(form.errors)

	return render(request, 'daftar_resto.html', context)

def updateMenu(request, id_menu):
	update_menu = Menu.objects.get(id=id_menu)

	data = {
		'nama_menu':update_menu.nama_menu,
		'harga':update_menu.harga,
	}

	update_menu_form = MenuForm(request.POST or None, initial=data, instance=update_menu)

	if request.method == 'POST':
		if update_menu_form.is_valid():
			update_menu_form.save()
		return redirect('resto', milik=request.user.id)

	context = {
		'update_menu_form' : update_menu_form,
	}
	print()
	return render(request, 'updateMenu.html', context)

def tambahMenu(request):
	form = MenuForm(request.POST or None)
	context = {
		'form':form,
	}
	if request.method == 'POST':
		if form.is_valid():
			menu_baru = form.save(commit=False)
			menu_baru.penyedia = Restorant.objects.get(milik=request.user)
			menu_baru.status = "Tersedia"
			menu_baru.save()
			return redirect('resto', milik=request.user.id)

		else:
			print("not valid")
			print(form.errors)

	return render(request, 'tambahMenu.html', context)

def deleteMenu(request, id_menu):
	delete_menu = Menu.objects.get(id=id_menu)
	delete_menu.delete() 

	return redirect('resto', milik=request.user.id)

def search(request):

	if 'query' in request.GET:
		query = request.GET['query']
		query = query.strip()
		resto_search = Restorant.objects.filter(nama_resto__icontains=query)
	
		context = {
			'q':query,
			'resto_search':resto_search,
		}

		return render(request, 'search.html', context)

	return redirect(index)

def logout_view(request):
    logout(request)
    return redirect('index')