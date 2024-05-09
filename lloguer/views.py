from django.shortcuts import render
from .models import Automobil
# Create your views here.

def viewAutomobil(request):
    automobils = Automobil.objects.all()
    return render(request, 'automobil_list.html', {'automobils': automobils})