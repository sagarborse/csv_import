from django.urls import path
from importer.views import CsvViewSet

urlpatterns = [
    path('', CsvViewSet.as_view(), name='lisy'),
]