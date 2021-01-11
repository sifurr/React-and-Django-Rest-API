# Models
from .models import Status

# Serializer based on Status Model
from .serializers import StatusSerializer

# rest_framework view instead of django builtin view
from rest_framework.response import Response

from rest_framework import generics, mixins


class StatusListCreateView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# to display a single post detail
class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    def put(request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
