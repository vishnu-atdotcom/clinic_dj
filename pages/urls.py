from django.urls import path
from .views import *

urlpatterns = [
    path('features',PagesView.as_view(),name='features'),
    path('team',TeamView.as_view(),name='Team'),
    path('appointment',Appointment.as_view(),name='Appointment'),
    path('testimonial',testimonial.as_view(),name='Testimonial'),
    path('doctor_list',Appointment.as_view(),name='Doctor_list'),
    
    path('error',error,name='404')
]
