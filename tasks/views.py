from rest_framework import generics, permissions
from tasks_api.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer

#GET and POST
class TaskList(generics.ListCreateAPIView):
  serializer_class = TaskSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Task.objects.all()

  def perform_create(self, serializer):
    serializer.save(task_owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()