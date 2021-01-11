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


# to display all the posts
class StatusListApiView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# to create post
class StatusCreateAPIView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# to display a single post detail
class StatusDetailAPIView(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)


# to update a single post
class StatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'


# to delete a single post
class StatusDeleteAPIView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'
