from rest_framework import serializers
from .models import Base, About, Gallery, OurProjects, HomeTitle, OurCoreServis, InfoDev


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = '__all__'
        read_only_fields = ('date_created', 'date_updated')


class HomeTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTitle
        fields = '__all__'


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


class OurCoreSevisSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurCoreServis
        fields = '__all__'

class InfoDevSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoDev
        fields = '__all__'