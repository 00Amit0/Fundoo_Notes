import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestRegistrationAPI:
    @pytest.mark.django_db
    def test_response_registration(self, client, django_user_model):

        url = reverse('register')
        # Register user
        data = {'username': 'At', 'password': '5677', 'email': 'am86@gmail.com',
                'phone_number': '1234567890', 'location': 'varanasi'}
        response = client.post(url, data, content_type="application/json")
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_response_login(self, client, django_user_model):
        django_user_model.objects.create_user(username='At', password='5677', email='am86@gmail.com',
                                              phone_number='1234567890', location='varanasi')
        url = reverse('log-in')
        # Login user
        data = {'username': 'At', 'password': '5677'}
        response = client.post(url, data, content_type="application/json")
        assert response.status_code == 202, 'Successfully logged in'

