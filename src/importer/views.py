from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Image
from .import_csv import  ImportCsv
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .serializers import ImageSerializer


# Create your views here.


class CsvViewSet(ListAPIView):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authenticatiopn_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        im = ImportCsv()
        im.import_csv_to_db()
        return super().get(*args, **kwargs)

