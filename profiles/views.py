from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from tasks_api.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]