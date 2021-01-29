from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response

from . import serializers
from .serializers import TaskSerializer
from .models import Task


# Create your views here.


class ApiOverview(APIView):

    def get(self, request):
        api_urls = {
            'List': '/task-list/',
            'Detail View': '/task-detail/task:<str:pk>/',
            'Create': '/task-create/',
            'Update': '/task-update/task:<str:pk>/',
            'Delete': '/task-delete/task:<str:pk>/',
        }
        return Response(api_urls)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAdminUser]


class TaskDetailView(APIView):

    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer


class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'


class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
