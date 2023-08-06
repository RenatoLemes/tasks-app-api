from django.urls import path, include
from tasks import views
from rest_framework.routers import DefaultRouter
from .views import TasksList

router = DefaultRouter()
router.register(r'tasks', TasksList, basename='tasks' )


urlpatterns = [
  path('', include(router.urls))
]