from django.shortcuts import render
from django.http import HttpResponse

def log_in_button(request):
    return HttpResponse('<a href=http://127.0.0.1:8000/mylibrary/login/><button type="button", style="background-color:#7CFC00">Log In</button></a>')

def log_in_interface(request):
    return render(request, 'mylibrary_app/index.html')
    # return HttpResponse('<button type="button", style="background-color:#7CFC00">Use your login</button>')

def user(requset, user_id):
    return HttpResponse(f"<h1>Here will be displayed user {user_id}'s library.</h1>")