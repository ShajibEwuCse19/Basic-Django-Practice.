from django.http import HttpRequest, HttpResponse, response
from django.shortcuts import render


# Create your views here.
def home(request):
    diction = {}
    return render(request, 'myApp/index.html', context=diction)


