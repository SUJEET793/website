from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the tutorial index function calling.")
def printname(request):
    return HttpResponse("<h1>Hi sujeet</h1>")
