from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Worker
from .serializers import WorkerSerializer


class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
