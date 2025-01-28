from django.db import models
import uuid

class Doctor(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    doctor_name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)
    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.doctor_name
    
class Appointments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    doctor_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    mobile = models.CharField(max_length=15, null=False, blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)  # Foreign key relation with Doctor
    date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.doctor.doctor_name}"