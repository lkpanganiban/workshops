import uuid
from rest_framework import serializers
from .models import WorldBorder
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class WorldBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = "mpoly"

        fields = "__all__"
