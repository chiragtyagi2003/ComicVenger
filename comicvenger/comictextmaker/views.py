from django.shortcuts import render

# Create your views here.

# index view
def index(request):
    return render(request, 'comictextmaker/index.html')


def home(request):
    return render(request, 'comictextmaker/home.html')