from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import ProjectModelSerializer, MeasurementsModelSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsModelSerializer
