from rest_framework import viewsets
from .models import RehabCenter, Patient, Interview
from .serializers import RehabCenterSerializer, PatientSerializer, InterviewSerializer

class RehabCenterViewSet(viewsets.ModelViewSet):
    queryset = RehabCenter.objects.all()
    serializer_class = RehabCenterSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer