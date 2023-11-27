from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RehabCenterViewSet, PatientViewSet, InterviewViewSet

router = DefaultRouter()
router.register(r'rehab_centers', RehabCenterViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'interviews', InterviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]