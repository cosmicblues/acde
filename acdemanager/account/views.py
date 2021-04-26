from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def form(request):
    return render(request, 'accounts/form.html')

def profile(request):
    return render(request, 'accounts/profile.html')
