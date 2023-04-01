from django.urls import path 
from .views import *


urlpatterns = [
    path('api/', BaseSerializerAPI.as_view()),
    path('about/', AboutSerializerAPI.as_view()),
    path('gallery/', GalerrySerializerAPI.as_view()),
    path('our/', OurProjectsSerializerAPI.as_view()),
    path('hometitle/', HomeTitleSerializerAPI.as_view()),
    path('ourservis/', OurCoreSevisSerializerAPI.as_view()),
    path('info/', InfoDevSerializerAPI.as_view()),

    # detail update url
    path('api/<int:pk>/', BaseUpdatedSerializer.as_view()),
    path('about/<int:pk>/', AboutUpdatedSerializer.as_view()),
    path('gallery/<int:pk>/', GalleryUpdatedSerializer.as_view()),
    path('our/<int:pk>/', OurUpdatedSerializer.as_view()),
    path('hometitle/<int:pk>/', HomeTitleUpdateSerializerAPI.as_view()),
    path('ourservis/<int:pk>/', OurCoreSevisUpdateSerializerAPI.as_view()),
    path('info/<int:pk>/', InfoUpdateSerializerAPI.as_view()),

]


