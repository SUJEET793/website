from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = request.GET['your_name']
    return render(request, "home.html", {'name': name})


def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    if val1==None and val2==None:
        return render(request, "result.html", {'result':"pleasse enter valit input"})
    result = val1 + val2
    return render(request, "result.html", {'result': result})


def name(request):
    return render(request, "name.html")
