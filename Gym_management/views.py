# views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Gym, Trainer, Client, WorkoutSession
from .serializers import GymSerializer, TrainerSerializer, ClientSerializer, WorkoutSessionSerializer


def home(request):
    return render(request, 'Gym_management/home.html')


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
