import json
import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


@pytest.fixture
def authentication_user(client, django_user_model):
    user = django_user_model.objects.create_user(username='At', password='5677', phone_number=1234567890,
                                                 location='varanasi')
    url = reverse('log-in')
    data = {'username': 'At', 'password': '5677'}
    client.post(url, data)
    return user.id


class TestNoteAppCrudOperation:
    @pytest.mark.django_db
    def test_post_user_with_success_response(self, client, django_user_model, authentication_user):
        user_id = authentication_user
        url = reverse("all")
        data = {"title": "Daydreamer", "description": "Living in dreams", "user": user_id}
        response = client.post(url, data, content_type='application/json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_note_get_api_response(self, client, authentication_user):
        user_id = authentication_user
        url = reverse("all")
        data = {"title": "Daydreamer", "description": "Living in dreams", "user": user_id}
        response = client.post(url, data, content_type='application/json')
        assert response.status_code == 201
        url = reverse('all')
        url = url + '?user_id=' + str(user_id)
        response = client.get(url, content_type='application/json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_note_put_api_response(self, client, authentication_user):
        user_id = authentication_user
        url = reverse("all")
        data = {"title": "Daydreamer", "description": "Living in dreams", "user": user_id}
        response = client.post(url, data, content_type='application/json')
        json_data = json.loads(response.content)
        note_id = json_data.get('data').get('id')
        assert response.status_code == 201
        url = reverse("all")
        data = {"id": note_id, "title": "Hello", "description": "Manners", "user": user_id}
        response = client.put(url, data, content_type='application/json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_note_delete_response(self, client, authentication_user):
        user_id = authentication_user
        url = reverse("all")
        data = {"title": "Daydreamer", "description": "Living in dreams", "user": user_id}
        response = client.post(url, data, content_type='application/json')
        json_data = json.loads(response.content)
        assert response.status_code == 201
        note_id = json_data.get('data').get('id')
        url = reverse("all")
        data = {'id': note_id}
        response = client.delete(url, data, content_type='application/json')
        assert response.status_code == 204
        assert response.data == {'data': 'deleted'}
