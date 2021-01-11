from django.urls import path
from .views import (
    StatusAPIView,
    StatusListApiView,
    StatusCreateAPIView,
    StatusDetailAPIView,
    StatusUpdateAPIView,
    StatusDeleteAPIView,
)

urlpatterns = [
    path('status/', StatusAPIView.as_view()),
    path('status/list/', StatusListApiView.as_view()),
    path('status/create/', StatusCreateAPIView.as_view()),
    path('status/detail/<id>/', StatusDetailAPIView.as_view()),
    path('status/update/<id>/', StatusUpdateAPIView.as_view()),
    path('status/delete/<id>/', StatusDeleteAPIView.as_view()),
]
