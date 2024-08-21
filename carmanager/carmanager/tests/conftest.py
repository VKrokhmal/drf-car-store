import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register
from .factories import CategoryFactory, CarFactory, BrandFactory

register(CategoryFactory)
register(BrandFactory)
register(CarFactory)


@pytest.fixture
def api_client():
    return APIClient
