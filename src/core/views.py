# Create your views here.
from django.shortcuts import render


def home_page(request):
    # return HttpResponse("<html><title>Fast Style</title></html>")
    return render(request, "home.html")
