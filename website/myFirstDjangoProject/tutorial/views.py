from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    for x in range(3):
        return render(request, 'home.html', {'name': x})
