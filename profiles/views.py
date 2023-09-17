from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from tasks_api.permissions import IsProfileOwnerOrReadOnly

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrReadOnly]