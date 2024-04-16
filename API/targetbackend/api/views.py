from django.shortcuts import render # type: ignore
from rest_framework import generics # type: ignore
from .models import JobPost
from .serializers import JobPostSerializer

#usercreation
from django.contrib.auth.forms import UserCreationForm   # type: ignore




class JobPostListCreate(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

class JobPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    lookup_field = "pk"

