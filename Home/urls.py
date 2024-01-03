

from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.HomePage,name='HomePage'),
    path('Donate/',views.donation,name='donation'),
]
