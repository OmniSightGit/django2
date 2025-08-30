import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_render_admin_login(client: Client):
    url = reverse("admin:login")

    response = client.get(url)

    assert response.status_code == 200
