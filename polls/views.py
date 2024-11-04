from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, món. Ests a l'índex d'enquestes!")
