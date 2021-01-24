"""EATINGOUT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.search, name='search'),
    path('', views.index, name="index"),
    path('homepage/', views.homepage, name="homepage"),
    path('resto/<str:milik>', views.resto, name="resto"),
    path('updateMenu/<int:id_menu>', views.updateMenu, name="updateMenu"),
    path('tambahMenu/', views.tambahMenu, name="tambahMenu"),
    path('deleteMenu/<int:id_menu>', views.deleteMenu, name="deleteMenu"),
    path('login/', include('accounts.urls')) ,
    path('daftarresto/', views.daftarresto, name="daftarresto"),   
    path('logout/', views.logout_view, name="logout"),   
    path('rubah_menu/<str:id_menu>', views.rubah_menu, name='rubah_menu'),
    path('resto_status/<str:id_resto>', views.resto_status, name='resto_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)