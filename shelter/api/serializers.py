from rest_framework import serializers
from project.models import Vulnerability

class VulnerabilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vulnerability
        fields = ['id', 'hostname', 'ip_address', 'title', 'severity', 'cvss', 'publication_date']