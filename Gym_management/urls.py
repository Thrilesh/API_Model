# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GymViewSet, TrainerViewSet, ClientViewSet, WorkoutSessionViewSet
from Gym_management.views import home

router = DefaultRouter()
router.register(r'gyms', GymViewSet, basename='gyms-list')
router.register(r'trainers', TrainerViewSet, basename='trainers-list')
router.register(r'clients', ClientViewSet, basename='clients-list')
router.register(r'workouts', WorkoutSessionViewSet, basename='workouts-list')

urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('api/', include(router.urls)),  # API URLs
]
