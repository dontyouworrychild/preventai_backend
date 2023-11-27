from rest_framework import serializers
from .models import RehabCenter, Patient, Interview

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