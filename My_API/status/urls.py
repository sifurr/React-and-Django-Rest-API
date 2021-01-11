from django.urls import path
from .views import StatusCrudWithViewsets
from rest_framework.routers import DefaultRouter

# status/ -> List, Create -> GET, POST
# ststus/<id>/ -> Details, Delete, Update -> GET, DELETE, PUT/PATCH

router = DefaultRouter()
router.register(r'status', StatusCrudWithViewsets, basename='status')


urlpatterns = [] + router.urls
