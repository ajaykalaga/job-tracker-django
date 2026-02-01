from django.shortcuts import render
from .models import JobApplications
from .serializers import JobApplicationSerializer
from rest_framework import generics,permissions
# Create your views here.

class JobListCreateView(generics.ListCreateAPIView):
  serializer_class = JobApplicationSerializer
  permissions_classes = [permissions.IsAuthenticated]
  def get_queryset(self):
    return JobApplications.objects.filter(user=self.request.user)
  
  def perform_create(self,serializer):
    serializer.save(user=self.request.user)
