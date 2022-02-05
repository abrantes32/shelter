from rest_framework import viewsets
from rest_framework import permissions
from shelter.api.serializers import VulnerabilitySerializer
from project.models import Vulnerability

class VulnerabilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer
    permission_classes = [permissions.IsAuthenticated]