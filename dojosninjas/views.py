from .models import *
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context={
        'ninjas': Ninja.objects.all(),
        'dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def submitninja(request):
    print(request.POST)
    Ninja.objects.create(
        name=request.POST['ninjaname'],
        age=request.POST['age'],
        dojo=Dojo.objects.get(id=request.POST['dojoid'])
    )
    return redirect('/')

def submitdojo(request):
    print(request.POST)
    Dojo.objects.create(
        name=request.POST['dojoname'],
        city=request.POST['dojocity']
    )
    return redirect('/')