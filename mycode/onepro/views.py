from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'onepro/index.html')

def new(request):
    return render(request, 'onepro/new.html')