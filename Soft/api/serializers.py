from rest_framework import serializers
from .models import Base


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = '__all__'
        read_only_fields = ('date_created', 'date_updated')
