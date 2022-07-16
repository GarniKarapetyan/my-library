from django.shortcuts import render
from django.http import HttpResponse


from .models import *
# menu = ['Logo', 'News', 'Base Library', 'About', 'Connection', 'Registration']
menu = [
    {'title': 'Logo', 'url_name': 'home'},
    {'title': 'News', 'url_name':'news'},
    {'title': 'Base Library', 'url_name': 'libraries'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Registration', 'url_name': 'registration'},
]


def home(request):
    context = {'menu': menu}
    return render(request, 'mylibrary_app/home.html', context=context)
    # return HttpResponse('<a href=http://127.0.0.1:8000/mylibrary/login/><button type="button", style="background-color:#7CFC00">Log In</button></a>')

def client(request):
    posts = Libraries.objects.all()
    context = {'posts': posts, 'menu': menu}
    return render(request, 'mylibrary_app/client.html', context=context)
    # return HttpResponse('<button type="button", style="background-color:#7CFC00">Use your login</button>')

def news(request):
    posts = Libraries.objects.all()
    context = {'posts': posts, 'menu': menu}
    return render(request, 'mylibrary_app/news.html', context=context)

def all_libraries(request):
    posts = Libraries.objects.all()
    context = {'posts': posts, 'menu': menu}
    return render(request, 'mylibrary_app/all_libraries.html', context=context)

def about(request):
    posts = Libraries.objects.all()
    context = {'posts': posts, 'menu': menu}
    return render(request, 'mylibrary_app/about.html', context=context)

def registration(request):
    posts = Libraries.objects.all()
    context = {'posts': posts, 'menu': menu}
    return render(request, 'mylibrary_app/registration.html', context=context)

def user(requset, user_id):
    return HttpResponse(f"<h1>Here will be displayed user {user_id}'s library.</h1>")