from rest_framework import filters, status, viewsets
from .models import User
from .serializers import ListUserSerializer
from rest_framework.permissions import AllowAny

class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    permission_classes = [AllowAny]