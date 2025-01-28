from django.urls import path
from .views import *

urlpatterns = [
    path('', AboutView.as_view(), name='about_clinic'),
    path('services/',ServicesView.as_view(),name='services'),
    path('contact/',ContactView.as_view(),name='contact')
]