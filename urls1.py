"""website1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render


def home(request):
    return render(request, 'accounts/homepage1.html')


def contact(request):
    return render(request, 'accounts/about.html')


def trial(request):
    return render(request, 'accounts/trial.html')


def coming_soon(request):
    return render(request, 'accounts/coming_soon.html')


urlpatterns = [
    path('game/', include('game.urls')),
    path('', home, name='home'),
    path('about/', contact, name='about'),
    path('trial/', trial),
    path('coming_soon/', coming_soon, name='coming_soon')
]
