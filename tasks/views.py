from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TasksList(viewsets.ModelViewSet):
  # queryset = Task.objects.all()
  serializer_class = TaskSerializer
  permission_classes = [IsAuthenticated]
  def get_queryset(self):
    return Task.objects.filter(task_owner=self.request.user)
  # def get(self, request):
  #   tasks = Task.objects.all()
  #   serializer = TaskSerializer(tasks, many=True, context={'request': request})
  #   return Response(serializer.data)

  # def post(self, request):
  #   serializer = TaskSerializer(data=request.data, context={'request': request})
  #   if serializer.is_valid():
  #       serializer.save()
  #       return Response(serializer.data, status=status.HTTP_201_CREATED)
  #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class TasksList(APIView):
#   serializer_class = TaskSerializer
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#   queryset = Task.objects.all().order_by('-due_date')
#   def get(self, request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True, context={'request': request})
#     return Response(serializer.data)

#     def post(self, request):
#       serializer = TaskSerializerSerializer(
#         data=request.data, context={'request': request}
#       )
#       if serializer.is_valid():
#         serializer.save(owner=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
      
#     return Response(
#       serializer.errors, status=status.HTTP_404_BAD_REQUEST
#     )






  # def get_queryset(self):
      
  #   queryset = Task.objects.all()
  #   state = self.request.query_params.get('state', None)
  #   priority = self.request.query_params.get('priority', None)

  #   if state is not None:
  #       queryset = queryset.filter(state=state)

  #   if priority is not None:
  #       queryset = queryset.filter(priority=priority)

  #   return queryset