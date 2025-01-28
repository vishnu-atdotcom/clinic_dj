
from django.contrib import admin
from .models import Doctor, Appointments

class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'email', 'mobile', 'date', 'description')  # Columns to show in list view
    list_filter = ('doctor', 'date')  # Add filters for doctor and date
    search_fields = ('email', 'mobile', 'doctor__doctor_name')  # Add search fields

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'department', 'image', 'facebook', 'twitter', 'instagram')  # Customize fields shown

# Register the models with custom admin interfaces
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointments, AppointmentsAdmin)
