from django.urls import path
from .views import home

urlpatterns = [
    path('hola/', home, name='hola'),
]
