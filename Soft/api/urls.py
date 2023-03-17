from django.urls import path 
from .views import *


urlpatterns = [
    path('api/', BaseSerializerAPI.as_view()),
    path('api/<int:pk>/', BaseDetailApi.as_view()),
    path('change/<int:pk>/', BaseUpdatedSerializer.as_view()),
]


