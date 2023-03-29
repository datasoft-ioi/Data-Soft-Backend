from django.urls import path 
from .views import *


urlpatterns = [
    path('api/', BaseSerializerAPI.as_view()),
    path('about/', AboutSerializerAPI.as_view()),
    path('gallery/', GalerrySerializerAPI.as_view()),
    path('our/', OurProjectsSerializerAPI.as_view()),
    path('hometitle/', HomeTitleSerializerAPI.as_view()),
    path('ourservis/', OurCoreSevisSerializerAPI.as_view()),

    # detail update url
    path('change/<int:pk>/', BaseUpdatedSerializer.as_view()),
    path('about/<int:pk>/', AboutUpdatedSerializer.as_view()),
    path('gallery/<int:id>/', GalleryUpdatedSerializer.as_view()),
    path('our/<int:id>/', OurUpdatedSerializer.as_view()),
    path('hometitle/<int:id>/', HomeTitleUpdateSerializerAPI.as_view()),
    path('ourservis/<int:id>/', OurCoreSevisUpdateSerializerAPI.as_view())

]


