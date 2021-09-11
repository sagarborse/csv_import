from django.urls import path
from importer.views import CsvViewSet

urlpatterns = [
    path('images/', CsvViewSet.as_view(), name='list_images'),
]