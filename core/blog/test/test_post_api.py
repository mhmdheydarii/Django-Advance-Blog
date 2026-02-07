from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from accounts.models import User

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email="admin@admin.com", password="!@#$5678")
    return user

@pytest.mark.django_db
class TestPostApi:
    client = APIClient()
    
    def test_get_post_response_200(self):
        url = reverse('blog:api:post-list')
        response = self.client.get(url)
        assert response.status_code == 200
    
    def test_create_post_response_400(self):
        url = reverse("blog:api:post-list")
        data = {
            "title" : "test",
            "content" : "hi",
            "status" : True,
            "published_date" : datetime.now()
        }
        self.client.force_authenticate(user={})
        response = self.client.post(url, data)
        assert response.status_code == 400