from rest_framework import serializers
from .models import Base, About, Gallery, OurProjects


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = '__all__'
        read_only_fields = ('date_created', 'date_updated')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'



class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'



class OurProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurProjects
        fields = '__all__'

