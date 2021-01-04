#alternatywnie views.py zamiast generics

from rest_framework import viewsets
from .models import DataSet
from .serializers import DataSerializers, UserSerializers
from .permissionsuser import IsUserOwnerReadOnly

from django.contrib.auth import get_user_model

class PostViewSet(viewsets.ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSerializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers