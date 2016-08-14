from django.conf import settings
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', { 'page': 'home' })


def about(request):
    return render(request, 'about.html', { 'page': 'about' })


def jobs(request):
    return render(request, 'jobs.html', { 'page': 'jobs' })


def contact(request):
    return render(request, 'contact.html', { 'page': 'contact' })
