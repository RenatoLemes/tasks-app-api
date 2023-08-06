from rest_framework import generics, permissions
from tasks_api.permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer

#GET and POST
class TaskList(generics.ListCreateAPIView):
  serializer_class = TaskSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Task.objects.all()

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


#Retrieve, update and delete ----- video CommentList and CommentDetail generic views

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()



#////////////////////////////////////////////

# from rest_framework import status, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Task
# from .serializers import TaskSerializer
# from tasks_api.permissions import IsOwnerOrReadOnly


# class TaskList(APIView):
#   serializer_class = TaskSerializer
#   permission_classes = [
#     permissions.IsAuthenticatedOrReadOnly
#   ]
#   # this def get will get all tasks
#   def get(self, request):
#     tasks = Task.objects.all()
#     self.check_object_permissions(self.request, tasks) #maybe delete
#     serializer = TaskSerializer(
#       tasks, many=True, context={'request': request}
#     )
#     return Response(serializer.data)

#     # this will allow the user to create tasks
#   def post(self,request):
#     serializer = TaskSerializer(
#       data=request.data, context={'request': request}
#     )
#     if serializer.is_valid():
#         serializer.save(owner=request.user)
#         return Response(
#             serializer.data, status=status.HTTP_201_CREATED
#         )
#     return Response(
#         serializer.errors, status=status.HTTP_400_BAD_REQUEST
#     )

#///////////////////////////////////////////////////


# from rest_framework.views import APIView
# from rest_framework import viewsets
# from rest_framework.response import Response
# from .models import Task
# from .serializers import TaskSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication

# class TasksList(viewsets.ModelViewSet):
#   authentication_classes = [JWTAuthentication]
#   # queryset = Task.objects.all()
#   serializer_class = TaskSerializer
#   permission_classes = [IsAuthenticated]
#   def get_queryset(self):
#     return Task.objects.filter(task_owner=self.request.user)
 






