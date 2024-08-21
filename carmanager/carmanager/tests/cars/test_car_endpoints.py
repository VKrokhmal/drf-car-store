import json

import pytest

pytestmark = pytest.mark.django_db


class TestCarEndpoint:
    cars_endpoint = "/cars/"

    def test_cars_get(self, car_factory, api_client):
        car_factory.create_batch(4)
        response = api_client().get(self.cars_endpoint)
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:
    brand_endpoint = "/brands/"

    def test_brands_get(self, brand_factory, api_client):
        brand_factory.create_batch(4)
        response = api_client().get(self.brand_endpoint)
        print(json.loads(response.content))
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestCategoryEndpoints:
    category_endpoint = "/categories/"

    def test_category_get(self, category_factory, api_client):

        category_factory.create_batch(4)
        response = api_client().get(self.category_endpoint)
        print(json.loads(response.content))
        assert response.status_code == 200
