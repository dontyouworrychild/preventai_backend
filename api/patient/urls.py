from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'rehab_centers', RehabCenterViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'interviews', InterviewViewSet)
router.register(r'time_slots', TimeSlotViewSet)
router.register(r'doctrs', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]