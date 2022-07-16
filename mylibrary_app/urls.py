from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('client/', client, name='client'),
    path('news/', news, name='news'),
    path('libraries/', all_libraries, name='libraries'),
    path('about/', about, name='about'),
    path('registration/', registration, name='registration'),
    path('<slug:user_id>/', user)

]