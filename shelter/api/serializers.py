from django.contrib.auth.models import User, Group
from rest_framework import serializers
from project.models import Vulnerability


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class VulnerabilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vulnerability
        fields = ['id', 'hostname', 'ip_address', 'title', 'severity', 'cvss', 'publication_date']