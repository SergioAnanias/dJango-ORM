from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def books(request):
    context={
        'books': Book.objects.all(),
    }
    return render(request, 'books.html', context)

def authors(request):
    context={
        'authors': Author.objects.all(),
    }
    return render(request,'authors.html',context)

def book(request, num):
    book= Book.objects.get(id=num)
    context={
        'book': book,
        'authors': book.Authors.all(),
        'allauthors': Author.objects.all()
    }
    return render(request,'book.html', context)

def author(request, num):
    author = Author.objects.get(id=num)
    context={
        'author': author,
        'books': author.books.all(),
        'allbooks': Book.objects.all()
    }
    return render(request,'author.html', context)

def createbook(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc']
    )
    return redirect('/books')

def createauthor(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )
    return redirect('/authors')

def updatebook(request, num):
    book= Book.objects.get(id=num)
    authortoadd= request.POST['authortoadd']
    authortoadd = Author.objects.get(id=authortoadd)
    book.Authors.add(authortoadd) 
    book.save()
    return redirect(f'/books/{num}')

def updateauthor(request, num):
    author=Author.objects.get(id=num)
    booktoadd=request.POST['booktoadd']
    booktoadd = Book.objects.get(id=booktoadd)
    author.books.add(booktoadd)
    author.save()
    return redirect(f'/authors/{num}')