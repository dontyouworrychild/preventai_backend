import uuid
import datetime
from django.utils.translation import gettext_lazy as _
from django.db import models
from user.models import User

def patient_directory_path(instance, filename):
    extension = filename.split('.')[-1]
    return f"patients/{instance.id}.{extension}"

GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

class RehabCenter(models.Model):
    name = models.CharField()
    city = models.CharField()
    address = models.CharField()
    rating = models.IntegerField()

class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    image = models.ImageField(upload_to=patient_directory_path, blank=True)
    date_of_birth = models.DateField()
    
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    ethnicity = models.CharField(max_length=100)

    start_rehab_date = models.DateField()
    end_rehab_date = models.DateField()

    rehab_center = models.ForeignKey(RehabCenter, on_delete=models.CASCADE, related_name='patients')
    doctor_fio = models.CharField()

class Interview(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='interviews')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interviews')
    questions = models.TextField()
    feedback = models.TextField()
    percentage = models.IntegerField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Doctor(User):
    rating = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField()

    def save(self, *args, **kwargs):
        self.role = 'doctor'
        super().save(*args, **kwargs)


class TimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='time_slots')
    day_of_week = models.CharField(max_length=9, choices=[
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday')
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()