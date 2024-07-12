

from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.HomePage,name='HomePage'),
    path('Donate/',views.donation,name='donation'),
    path('Volunteer/',views.volunteer,name='volunteer'),
    path('SpansorShip/',views.SpansorShip,name='SpansorShip'),
    path('Mission/',views.Mission,name='Mission'),
    path('our-story/',views.ourStory,name='ourStory,'),
    path('Socail-support',views.socail_support,name='socail_support'),
    path('art',views.art,name='art'),
    path('contact/',views.contact,name='contact')
]
