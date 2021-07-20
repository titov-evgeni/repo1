from django.urls import path
from .views import base, output

urlpatterns = [
    path('', base, name='base'),
    path('output/', output, name='output'),
]
