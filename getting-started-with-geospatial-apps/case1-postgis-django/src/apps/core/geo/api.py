import json
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework_tracking.mixins import LoggingMixin
from .serializers import WorldBorderSerializer, WorldBorder


class WorldBorderViewset(LoggingMixin, viewsets.ModelViewSet):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer

    def should_log(self, request, response):
        """Log only errors"""
        return response.status_code >= 400
