from rest_framework import serializers

from .models import Employees, Image

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('id', 'title', 'user_id', 'created_at', 'updated_at', 'image_encoding')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)