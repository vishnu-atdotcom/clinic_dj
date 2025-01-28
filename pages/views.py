from django.shortcuts import render
from datetime import datetime
from django.views import View
from .models import Doctor,Appointments
from django.http import HttpResponse
from .utils import get_doctorlist


class PagesView(View):
    def get(self,request):
        return render (request ,'pages/feature.html')
    
class TeamView(View):
    
    def get(self,request):
        doctors=get_doctorlist()
        return render(request,'pages/team.html', doctors)
    
    
class Appointment(View):
    def get(self,request):
        doctors=get_doctorlist()
        return render(request,'pages/Appointment.html',doctors)
        
    def post(self,request):
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        doctor_id=request.POST.get('doctor')
        date=request.POST.get('date')
        description=request.POST.get('description','')

        try:
            date_obj=datetime.strptime(date,'%m/%d/%Y %I:%M %p')
            formated_time=date_obj.strftime('%Y-%m-%d %H:%M')
        except ValueError:
            return HttpResponse('Invalid date format. Please correct proper one')
        
        try:
            doctor=Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            return render(request,'pages/404.html') #Http404('Doctor not found')
            
        appointment=Appointments.objects.create(
            doctor_name=doctor.doctor_name,
            email=email,
            name=name,
            mobile=mobile,
            doctor=doctor,
            date=formated_time,
            description=description
        )

        return render(request, 'pages/appointment_success.html', {'appointment': appointment})
    
class testimonial(View):
    def get(self,request):
        return render(request,'pages/testimonial.html')
    
    
    
def error(request):
    return render (request,'pages/404.html')
    