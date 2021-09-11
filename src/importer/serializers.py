from rest_framework import serializers
from .models import CsvFile, Image, Client


class CsvFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvFile
        fields = ['url', 'uploaded', 'activate', 'client']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'title', 'description', 'client', 'created']

