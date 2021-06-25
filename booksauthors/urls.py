"""ormqueries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('authors', views.authors),
    path('books/<int:num>', views.book),
    path('authors/<int:num>', views.author),
    path('addbook', views.createbook),
    path('addauthor', views.createauthor),
    path('books/<int:num>/update', views.updatebook),
    path('authors/<int:num>/update', views.updateauthor),
]
