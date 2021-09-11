from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from .models import Image, Client, CsvFile
from rest_framework.test import force_authenticate
from . import views

class ModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(name='Customer A')
        client = Client.objects.get(id=1)
        CsvFile.objects.create(url='http://google.com/abc.csv', activate=True, client=client)
        Image.objects.create(image='http://test.com/abc.jpg', title='Item 1', description='This is a test', client=client)

    def test_title_label(self):
        image = Image.objects.get(id=1)
        field_label = image._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

class CsvViewSetTest(TestCase):
    def test_authorization(self):
        factory = APIRequestFactory()
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        view = views.CsvViewSet.as_view()

        # Make an authenticated request to the view...
        request = factory.get('/api/v1/images/')
        force_authenticate(request, user=user)
        response = view(request)
        assert response.status_code == 200