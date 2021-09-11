from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .import_csv import  ImportCsv


# Create your views here.


class CsvViewSet(APIView):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        im_obj = ImportCsv()
        im_obj.import_csv_to_db()

        return Response({'hello': 'there'}, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        # data = {
        #     'task': request.data.get('task'),
        #     'completed': request.data.get('completed'),
        #     'user': request.user.id
        # }
        # serializer = TodoSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'hello2': 'there2'}, status=status.HTTP_400_BAD_REQUEST)
