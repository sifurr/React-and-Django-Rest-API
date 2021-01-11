# Models
from .models import Status

# Serializer based on Status Model
from .serializers import StatusSerializer

# rest_framework view instead of django builtin view
from rest_framework.response import Response

from rest_framework import viewsets, parsers


# Full CRUD application with a single class
class StatusCrudWithViewsets(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    paerser_classes = [parsers.FormParser, parsers.MultiPartParser]
