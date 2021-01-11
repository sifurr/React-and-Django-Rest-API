# Models
from .models import Status

# Serializer based on Status Model
from .serializers import StatusSerializer

# rest_framework view instead of django builtin view
from rest_framework.response import Response

from rest_framework import generics, parsers


class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    paerser_classes = [parsers.FormParser, parsers.MultiPartParser]


# to display a single post detail
class StatusDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'
