# Models
from .models import Status

# Serializer based on Status Model
from .serializers import StatusSerializer

# rest_framework view instead of django builtin view
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics


# Create your views here.
class StatusAPIView(APIView):
    # builtin method
    def get(self, request, format=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list, many=True)
        return Response(status_serializer.data)


class StatusListApiView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusCreateAPIView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
