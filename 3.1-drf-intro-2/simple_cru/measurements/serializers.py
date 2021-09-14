from rest_framework import serializers
from .models import Project, Measurement


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MeasurementsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

