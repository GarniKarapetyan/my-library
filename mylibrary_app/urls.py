from django.urls import path
from .views import *

urlpatterns = [
    path('', log_in_button),
    path('login/', log_in_interface),
    path('<slug:user_id>/', user)
]