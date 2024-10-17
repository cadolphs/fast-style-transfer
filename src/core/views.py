# Create your views here.
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<html><title>Fast Style</title></html>")
