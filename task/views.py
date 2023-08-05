from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TasksList(APIView):
  def get(self, request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

  def get_queryset(self):
      
    queryset = Task.objects.all()
    state = self.request.query_params.get('state', None)
    priority = self.request.query_params.get('priority', None)

    if state is not None:
        queryset = queryset.filter(state=state)

    if priority is not None:
        queryset = queryset.filter(priority=priority)

    return queryset