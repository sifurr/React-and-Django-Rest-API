from django.urls import path
from .views import StatusAPIView, StatusListApiView, StatusCreateAPIView

urlpatterns = [
    path('status/', StatusAPIView.as_view()),
    path('status/list/', StatusListApiView.as_view()),
    path('status/create/', StatusCreateAPIView.as_view()),
]
