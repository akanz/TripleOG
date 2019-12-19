from rest_framework import viewsets
from info import models
from .serializers import InfoSerializer

class InfoViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = InfoSerializer
