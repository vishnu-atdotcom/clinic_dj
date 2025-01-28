from .models import Doctor

def get_doctorlist():
    doctor=Doctor.objects.all()
    return {'doctors':doctor}