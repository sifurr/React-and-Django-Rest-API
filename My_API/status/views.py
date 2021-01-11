# Models
from .models import Status

# Serializer based on Status Model
from .serializers import StatusSerializer

# rest_framework view instead of django builtin view
from rest_framework.response import Response

from rest_framework import generics


class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# to display a single post detail
class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'
