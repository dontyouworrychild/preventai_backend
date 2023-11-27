from rest_framework import serializers
from .models import *

class RehabCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehabCenter
        fields = ['id', 'name', 'city', 'address', 'rating']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'