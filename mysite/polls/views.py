from django.http import HttpResponse


def index(request):
    return HttpResponse("Saludos al grupo de programación II desde el server de Django")