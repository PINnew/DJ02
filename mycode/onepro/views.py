from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'caption': 'Проект на Django'
    }
    return render(request, 'onepro/index.html', data)

def new(request):
    return render(request, 'onepro/new.html')