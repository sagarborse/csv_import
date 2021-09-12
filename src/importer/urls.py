from django.urls import path
from importer.views import CsvViewSet,TestViewSet

urlpatterns = [
    path('images/', CsvViewSet.as_view(), name='list_images'),
    path('test/', TestViewSet.as_view(), name='list_import'),
]
